import arxiv
import json
import sys
import os
from typing import List
from mcp.server.fastmcp import FastMCP

RESEARCH_PAPER_DIR = "research_papers"

mcp = FastMCP("research")


@mcp.tool()
def search_arxiv(topic: str, max_results: int = 5) -> List[str]:
    """
    Search for research papers on arXiv based on a topic ans store the information

    Args:
        topic (str): topic to search for in arXiv.
        max_results (int): Maximum number of results to return.

    Returns:
        List[dict]: A list of dictionaries containing paper information.
    """
    client = arxiv.Client()

    search_papers = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    research_papers = client.results(search_papers)

    #Create a directory for the topic
    path = os.path.join(RESEARCH_PAPER_DIR, topic.lower().replace(" ", "_"))
    os.makedirs(path, exist_ok=True)

    # Get the file path
    file_path = os.path.join(path, "research_papers_info.json")

    #Load the files
    try:
        with open(file_path, "r") as json_file:
            papers_info = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        papers_info = {}        

    #Process each paper and add the paper information to the dictionary
    papers_ids = []
    for paper in research_papers:
        papers_ids.append(paper.get_short_id())
        paper_info = {
            "title": paper.title,
            "summary": paper.summary,
            "authors": [author.name for author in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "pdf_url": paper.pdf_url
        }
        papers_info[paper.get_short_id()] = paper_info

    # Save the updated information back to the file
    with open(file_path, "w") as json_file:
        json.dump(papers_info, json_file, indent=2) 

    print(f"Research papers information saved to {file_path}")

    # Return the list of paper IDs      
    return papers_ids


@mcp.tool()
def get_paper_info(paper_id: str) -> str:
    """
    Get information about a specific research paper by its ID accross all topic directories.

    Args:
        paper_id (str): The ID of the research paper to retrieve information for.

    Returns:
        JSON object: A JSON object containing the paper information.
    """

    for object in os.listdir(RESEARCH_PAPER_DIR):
        object_path = os.path.join(RESEARCH_PAPER_DIR, object)
        if os.path.isdir(object_path):
            file_path = os.path.join(object_path, "research_papers_info.json") 
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r") as json_file:
                        papers_info = json.load(json_file)
                        if paper_id in papers_info:
                            return json.dumps(papers_info[paper_id], indent=4)
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    print(f"Error decoding JSON in {file_path}")
                    continue

    return f"Paper with ID {paper_id} not found in any topic directory."


if __name__ == "__main__":
    mcp.run(transport='stdio')




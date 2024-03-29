from pathlib import Path
from fondant.pipeline import Pipeline

BASE_PATH = "./fondant-artifacts"
Path(BASE_PATH).mkdir(parents=True, exist_ok=True)

pipeline = Pipeline(
    name="parlementaire-vragen",
    description="Retrieve pdf download links, download content, structure the content and index into vector DB.",
    base_path=BASE_PATH,
)

# STEP 1: FETCH THE PDF DOWNLOAD LINKS
# Use a custom reusable (container) component to fetch the links
# Todo: make lightweight component into a container
# OR: Directly use a custom lightweight component to fetch the links
from components import FetchLinks
links = pipeline.read(
    FetchLinks,
    arguments={
        "link": 'https://www.vlaamsparlement.be/ajax/document-overview?page=0&period=current_year_of_office&current_year_of_office_value=2022-2023&aggregaat%5B%5D=Vraag%20of%20interpellatie&aggregaattype%5B%5D=Schriftelijke%20vraag&thema%5B%5D=Natuur%20en%20Milieu',
        "pages": 1,
    }
)

# STEP 2: DOWNLOAD THE CONTENT OF THE PDFS USING THE LINKS
# Todo: create component that actually downloads the pdfs behind the links

# OR: (for testing purposes) use a reusable component to load the already downloaded pdfs (-> downloaded using ParlementaireVragen.py)
#raw_data = pipeline.read(
#    "load_from_pdf",
#    arguments={
#        "pdf_path": "/output_pdfs/natuur_en_milieu",
#    }
#)

# STEP 3: EXTRACT AND STRUCTURE THE TEXT USING REGEX
# Use the reusable component to structure the text (container: https://hub.docker.com/repository/docker/cascoopman/parlementaire_vragen_structure_text/general)
#clean_data = raw_data.apply(
#    "parlementaire_vragen_structure_text",
#)
# OR: Use the lightweight component to structure the data
#from lw_structure_text import StructureText
#clean_data = raw_data.apply(
#    StructureText,
#)
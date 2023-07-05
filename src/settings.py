from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Detect (caxah)"
PROJECT_NAME_FULL: str = "Detect (caxah)"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
INDUSTRIES: List[Industry] = [Industry.Energy()]
CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_YEAR: int = 2022
HOMEPAGE_URL: str = "https://universe.roboflow.com/s-o33ou/detect-caxah"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 657704
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/detect-caxah"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://universe.roboflow.com/s-o33ou/detect-caxah/dataset/1/download"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "Amplifier": [230, 25, 75],
    "CCLD:1-2": [60, 180, 75],
    "CCLD:2-3": [255, 225, 25],
    "CCLD:3-4": [0, 130, 200],
    "CCLD:4-5": [245, 130, 48],
    "CCLD:5-6": [145, 30, 180],
    "Car_Overlap": [70, 240, 240],
    "Coax-Cable": [240, 50, 230],
    "Diameter": [210, 245, 60],
    "EQLD:1-1": [250, 190, 212],
    "EQLD:1-2": [0, 128, 128],
    "EQLD:1-3": [220, 190, 255],
    "EQLD:1-4": [170, 110, 40],
    "Electric-Cable": [255, 250, 200],
    "Fiber-Equipment": [128, 0, 0],
    "Lowest Point of Attachment on Pole": [170, 255, 195],
    "Lowest Point of Attachment on Strand": [128, 128, 0],
    "Pole_Height": [255, 215, 180],
    "SLP": [0, 0, 128],
    "Street-Light": [128, 128, 128],
    "Telco-Cable": [255, 0, 0],
    "Wooden-Pole": [0, 0, 255]
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = "https://universe.roboflow.com/s-o33ou/detect-caxah/dataset/1/download"
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Roboflow community"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://universe.roboflow.com/s-o33ou"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings

from dotenv import load_dotenv
import os

load_dotenv()
token_clickup = os.getenv("TOKEN")
space_id = os.getenv("SPACE_ID")
URL_CLICKUP = "https://api.clickup.com/api/v2/"

HEADERS_CLICKUP = {
    "Content-Type": "application/json",
    "Authorization": f"{token_clickup}"
}
abs_path = os.path.abspath(__file__ + "../../../")
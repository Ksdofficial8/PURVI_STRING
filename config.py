from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","13404637"))
API_HASH = getenv("API_HASH","a069bf02806468fe18427ab6b9a3bb6c")

BOT_TOKEN = getenv("BOT_TOKEN","7158045860:AAGSSSf19LrcE63w_ju1OcWVMr77hYYvSMU")
OWNER_ID = int(getenv("OWNER_ID","6283192619"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND")
MUST_JOIN = getenv("MUST_JOIN","KSD_BOT_NETWORK")

import os
import requests
from dotenv import load_dotenv

# โหลดตัวแปรจาก .env
load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("RAPIDAPI_HOST")
BASE_URL = "https://jsearch–6bRBa3QguO5/api"  # ตรวจสอบให้ตรงกับ Host ที่ได้

def get_jobs(keyword: str, location: str = "", page: int = 1) -> dict:
    """
    ดึงข้อมูลตำแหน่งงานจาก RapidAPI JSearch
    :param keyword: คำค้นหา เช่น 'Python Developer'
    :param location: สถานที่ เช่น 'Bangkok'
    :param page: หมายเลขหน้า (pagination)
    :return: dict ของ JSON Response
    """
    url = f"{BASE_URL}/search"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    params = {
        "query": keyword,
        "location": location,
        "page": page
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # ถ้ามี error จะโยน HTTPError
        data = response.json()
        return data
    except requests.RequestException as e:
        # กรณี network, timeout, หรือ HTTP error
        print(f"[Job API] Error fetching jobs: {e}")
        return {}

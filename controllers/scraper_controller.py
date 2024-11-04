# controllers/scraper_controller.py
import time

from flask import Blueprint, jsonify, request
from services.scraper_service import scrape_tourist_data

scraper_bp = Blueprint('scraper', __name__, url_prefix='/scraper')

@scraper_bp.route('/scrape', methods=['GET'])
def scrape():
    pages = request.args.get('pages', default=1, type=int)
    for page in range(1,pages):
       url = f'https://travel.qunar.com/travelbook/list.htm?page={page}&order=hot_heat'  # 爬取的目标 URL
       attractions = scrape_tourist_data(url)
       time.sleep(2)
    return jsonify({'message': 'Data scraped successfully!'})

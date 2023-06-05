from requests import get
import csv
import json

item_id_list = list()

csv_file = "dashboard_data.csv"
dict_data = list()
csv_columns = [
    'site_id',
    'seller_id',
    'category_id',
    'permalink',
    'thumbnail',
    'price',
    'original_price',
    'currency_id',
    'accepts_mercadopago',
    'warranty',
    'available_quantity',
    'condition',
    'state',
    'shipping',
    'free_shipping',
    'attr_img_id',
    'attr_img_name',
    'attr_img_value_name',
    'attr_sound_id',
    'attr_sound_name',
    'attr_sound_value_name',
    'attr_brand_id',
    'attr_brand_name',
    'attr_brand_value_name',
    'attr_color_id',
    'attr_color_name',
    'attr_color_value_name',
    'attr_compatbl_id',
    'attr_compatbl_name',
    'attr_compatbl_value_name',
    'attr_dvices_id',
    'attr_dvices_name',
    'attr_dvices_value_name',
    'attr_format_id',
    'attr_format_name',
    'attr_format_value_name',
    'attr_ghz_id',
    'attr_ghz_name',
    'attr_ghz_value_name',
    'attr_gen_id',
    'attr_gen_name',
    'attr_gen_value_name',
    'attr_gen_id',
    'attr_gen_name',
    'attr_gen_value_name',
    'attr_res_id',
    'attr_res_name',
    'attr_res_value_name',
    'attr_model_id',
    'attr_model_name',
    'attr_model_value_name',
    'attr_sys_id',
    'attr_sys_name',
    'attr_sys_value_name',
    'attr_ports_id',
    'attr_ports_name',
    'attr_ports_value_name',
    'attr_blth_id',
    'attr_blth_name',
    'attr_blth_value_name',
    'attr_wifi_id',
    'attr_wifi_name',
    'attr_wifi_value_name'
    ]



products = ['chromecast', 'Apple TV', 'Amazon Fire TV']

url_search = 'https://api.mercadolibre.com/sites/MLA/search?q={}&limit=50#json'
url_item = 'https://api.mercadolibre.com/items/{}'
# url_items = 'https://api.mercadolibre.com/items/?ids={}'

for search in products:

    response = get(url_search.format(search)).content
    data = json.loads(response)

    for item_id in data['results']:
        item_id_list.append(item_id['id'])


for item_id in item_id_list:
    response = get(url_item.format(item_id)).content
    data = json.loads(response)

    attr_img_id = None
    attr_img_name = None
    attr_img_value_name = None
    attr_sound_id = None
    attr_sound_name = None
    attr_sound_value_name = None
    attr_brand_id = None
    attr_brand_name = None
    attr_brand_value_name = None
    attr_color_id = None
    attr_color_name = None
    attr_color_value_name = None
    attr_compatbl_id = None
    attr_compatbl_name = None
    attr_compatbl_value_name = None
    attr_dvices_id = None
    attr_dvices_name = None
    attr_dvices_value_name = None
    attr_format_id = None
    attr_format_name = None
    attr_format_value_name = None
    attr_ghz_id = None
    attr_ghz_name = None
    attr_ghz_value_name = None
    attr_gen_id = None
    attr_gen_name = None
    attr_gen_value_name = None
    attr_gen_id = None
    attr_gen_name = None
    attr_gen_value_name = None
    attr_res_id = None
    attr_res_name = None
    attr_res_value_name = None
    attr_model_id = None
    attr_model_name = None
    attr_model_value_name = None
    attr_sys_id = None
    attr_sys_name = None
    attr_sys_value_name = None
    attr_ports_id = None
    attr_ports_name = None
    attr_ports_value_name = None
    attr_blth_id = None
    attr_blth_name = None
    attr_blth_value_name = None
    attr_wifi_id = None
    attr_wifi_name = None
    attr_wifi_value_name = None

    site_id = data['site_id']
    seller_id = data['seller_id']
    category_id = data['category_id']

    permalink = data['permalink']
    thumbnail = data['thumbnail']

    price = data['price']
    original_price = data['original_price']
    currency_id = data['currency_id']
    accepts_mercadopago = data['accepts_mercadopago']
    warranty = data['warranty']

    available_quantity = data['available_quantity']
    condition = data['condition']

    state = data['seller_address']['state']['name']
    shipping = data['shipping']['mode']
    if data.get('free_shipping'):
        free_shipping = data['free_shipping']
    else:
        free_shipping = None

    for attr in data['attributes']:
        if attr['id'] == 'AUDIO_AND_VIDEO_INTERFACES':
            attr_img_id = attr['value_id']
            attr_img_name = attr['name']
            attr_img_value_name = attr['value_name']

        if attr['id'] == 'AUDIO_QUALITY':
            attr_sound_id = attr['value_id']
            attr_sound_name = attr['name']
            attr_sound_value_name = attr['value_name']

        if attr['id'] == 'BRAND':
            attr_brand_id = attr['value_id']
            attr_brand_name = attr['name']
            attr_brand_value_name = attr['value_name']

        if attr['id'] == 'COLOR':
            attr_color_id = attr['value_id']
            attr_color_name = attr['name']
            attr_color_value_name = attr['value_name']

        if attr['id'] == 'COMPATIBLE_APPLICATIONS':
            attr_compatbl_id = attr['value_id']
            attr_compatbl_name = attr['name']
            attr_compatbl_value_name = attr['value_name']

        if attr['id'] == 'COMPATIBLE_DEVICES':
            attr_dvices_id = attr['value_id']
            attr_dvices_name = attr['name']
            attr_dvices_value_name = attr['value_name']

        if attr['id'] == 'DEVICE_FORMAT':
            attr_format_id = attr['value_id']
            attr_format_name = attr['name']
            attr_format_value_name = attr['value_name']

        if attr['id'] == 'FREQUENCIES':
            attr_ghz_id = attr['value_id']
            attr_ghz_name = attr['name']
            attr_ghz_value_name = attr['value_name']

        if attr['id'] == 'GENERATION':
            attr_gen_id = attr['value_id']
            attr_gen_name = attr['name']
            attr_gen_value_name = attr['value_name']

        if attr['id'] == 'ITEM_CONDITION':
            attr_gen_id = attr['value_id']
            attr_gen_name = attr['name']
            attr_gen_value_name = attr['value_name']

        if attr['id'] == 'MAX_VIDEO_RESOLUTION':
            attr_res_id = attr['value_id']
            attr_res_name = attr['name']
            attr_res_value_name = attr['value_name']

        if attr['id'] == 'MODEL':
            attr_model_id = attr['value_id']
            attr_model_name = attr['name']
            attr_model_value_name = attr['value_name']

        if attr['id'] == 'OPERATING_SYSTEM':
            attr_sys_id = attr['value_id']
            attr_sys_name = attr['name']
            attr_sys_value_name = attr['value_name']

        if attr['id'] == 'PORTS_AND_CONNECTORS_TYPES':
            attr_ports_id = attr['value_id']
            attr_ports_name = attr['name']
            attr_ports_value_name = attr['value_name']

        if attr['id'] == 'WITH_BLUETOOTH':
            attr_blth_id = attr['value_id']
            attr_blth_name = attr['name']
            attr_blth_value_name = attr['value_name']

        if attr['id'] == 'WITH_WI_FI':
            attr_wifi_id = attr['value_id']
            attr_wifi_name = attr['name']
            attr_wifi_value_name = attr['value_name']
            
        
        dict_data.append({
            'site_id': site_id,
            'seller_id': seller_id,
            'category_id': category_id,
            'permalink': permalink,
            'thumbnail': thumbnail,
            'price': price,
            'original_price': original_price,
            'currency_id': currency_id,
            'accepts_mercadopago': accepts_mercadopago,
            'warranty': warranty,
            'available_quantity': available_quantity,
            'condition': condition,
            'state': state,
            'shipping': shipping,
            'free_shipping': free_shipping,
            'attr_img_id': attr_img_id,
            'attr_img_name': attr_img_name,
            'attr_img_value_name': attr_img_value_name,
            'attr_sound_id': attr_sound_id,
            'attr_sound_name': attr_sound_name,
            'attr_sound_value_name': attr_sound_value_name,
            'attr_brand_id': attr_brand_id,
            'attr_brand_name': attr_brand_name,
            'attr_brand_value_name': attr_brand_value_name,
            'attr_color_id': attr_color_id,
            'attr_color_name': attr_color_name,
            'attr_color_value_name': attr_color_value_name,
            'attr_compatbl_id': attr_compatbl_id,
            'attr_compatbl_name': attr_compatbl_name,
            'attr_compatbl_value_name': attr_compatbl_value_name,
            'attr_dvices_id': attr_dvices_id,
            'attr_dvices_name': attr_dvices_name,
            'attr_dvices_value_name': attr_dvices_value_name,
            'attr_format_id': attr_format_id,
            'attr_format_name': attr_format_name,
            'attr_format_value_name': attr_format_value_name,
            'attr_ghz_id': attr_ghz_id,
            'attr_ghz_name': attr_ghz_name,
            'attr_ghz_value_name': attr_ghz_value_name,
            'attr_gen_id': attr_gen_id,
            'attr_gen_name': attr_gen_name,
            'attr_gen_value_name': attr_gen_value_name,
            'attr_gen_id': attr_gen_id,
            'attr_gen_name': attr_gen_name,
            'attr_gen_value_name': attr_gen_value_name,
            'attr_res_id': attr_res_id,
            'attr_res_name': attr_res_name,
            'attr_res_value_name': attr_res_value_name,
            'attr_model_id': attr_model_id,
            'attr_model_name': attr_model_name,
            'attr_model_value_name': attr_model_value_name,
            'attr_sys_id': attr_sys_id,
            'attr_sys_name': attr_sys_name,
            'attr_sys_value_name': attr_sys_value_name,
            'attr_ports_id': attr_ports_id,
            'attr_ports_name': attr_ports_name,
            'attr_ports_value_name': attr_ports_value_name,
            'attr_blth_id': attr_blth_id,
            'attr_blth_name': attr_blth_name,
            'attr_blth_value_name': attr_blth_value_name,
            'attr_wifi_id': attr_wifi_id,
            'attr_wifi_name': attr_wifi_name,
            'attr_wifi_value_name': attr_wifi_value_name
        })


try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
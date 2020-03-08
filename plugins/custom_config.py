import os

from .utils import ReadJson, UpdateJson

SELF_ID = '2192720436'
MASTER = ['821480843']
MASTER_GROUP = ['861919492']

GROUP_PASSWORD = 'dnd5e-pear'

LOCAL_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
LOCAL_NICKNAME_PATH = os.path.join(LOCAL_DATA_PATH, 'nick_name.json')
LOCAL_INITINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'init_info.json')
LOCAL_PCSTATE_PATH = os.path.join(LOCAL_DATA_PATH, 'pc_state.json')
LOCAL_GROUPINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'group_info.json')

LOCAL_CUSTOM_DATA_PATH = os.path.join(os.path.dirname(__file__), 'custom_data')
LOCAL_QUERYINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'query_info')
LOCAL_DECKINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'deck_info')
LOCAL_MENUINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'menu_info')

GIFT_LIST = ['秘制蜜汁小鱼干', '吹起来很好听的小螺号', '特别美味的大青蟹',
 '珍贵的水晶球(听说吞下去可以转运)', '偷偷带出来的淬毒匕首', '父皇宝库里的幽蓝魔杖',
 '路上随便捡的一把生锈三叉戟', '超迷你皇冠(建国666周年纪念品)', '漂亮的鳞片(来源不明)',
 '椰蛋树牌椰汁', '最新的海底八卦杂志', '皇宫大殿的WiFi密码', '咸鱼味果冻', '母后偷偷在用的美白精华', '一瓶从六核之洋深处取来的海水',
 '古老的青铜镜子(边框上刻着铭文"阿罗德斯")']

MENU_CUISINE_LIST = ['经典', '精灵', '矮人', '东方', '异域']
MENU_TYPE_LIST = ['小菜', '主菜', '汤', '甜品', '酒', '饮料']
MENU_STYLE_LIST = ['黑暗', '野炊', '酒馆', '奢侈']
MENU_KEYWORD_LIST = MENU_CUISINE_LIST + MENU_TYPE_LIST + MENU_STYLE_LIST

COOK_FAIL_STR_LIST = ['略加思索', '灵机一动', '毫不犹豫', '啊!就是这个', '不如这样']


if os.path.exists(LOCAL_DATA_PATH) == False:
    os.makedirs(LOCAL_DATA_PATH)
    print("Make dir: " + LOCAL_DATA_PATH)

if os.path.exists(LOCAL_NICKNAME_PATH) == False:
    test_dict = {'TEST_personId':'Nickname'}
    UpdateJson(test_dict, LOCAL_NICKNAME_PATH)
    print("Create file: " + LOCAL_NICKNAME_PATH)
    del test_dict

if os.path.exists(LOCAL_INITINFO_PATH) == False:
    test_dict = {'TEST_groupId':'Init Info'}
    UpdateJson(test_dict, LOCAL_INITINFO_PATH)
    print("Create file: " + LOCAL_INITINFO_PATH)
    del test_dict
    
if os.path.exists(LOCAL_PCSTATE_PATH) == False:
    test_dict = {'TEST_personId':'PC State'}
    UpdateJson(test_dict, LOCAL_PCSTATE_PATH)
    print("Create file: " + LOCAL_PCSTATE_PATH)
    del test_dict

if os.path.exists(LOCAL_GROUPINFO_PATH) == False:
    test_dict = {'TEST_groupId':'Group Info'}
    UpdateJson(test_dict, LOCAL_GROUPINFO_PATH)
    print("Create file: " + LOCAL_GROUPINFO_PATH)
    del test_dict
    
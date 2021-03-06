dict_city = {'1': '百色', '3': '毕节', '5': '成都', '6': '池州', '7': '滁州', '8': '慈溪', '9': '东莞', '10': '佛山', '11': '抚州',
             '12': '广安', '13': '贵阳', '42': '上海', '15': '杭州', '16': '河池', '17': '河源', '18': '菏泽', '19': '湖州', '20': '怀化',
             '21': '惠州', '22': '济宁', '23': '揭阳', '24': '荆门', '25': '九江', '26': '昆明', '27': '兰州', '28': '六盘水',
             '29': '娄底', '30': '梅州', '31': '南昌', '32': '南平', '33': '宁波', '34': '宁德', '35': '宁海', '36': '平顶山',
             '37': '青岛', '38': '清远', '39': '泉州', '40': '厦门', '41': '汕头', '46': '石家庄', '43': '上饶', '44': '深圳',
             '45': '沈阳', '71': '镇江', '48': '台州', '49': '太原', '50': '泰安', '51': '铜陵', '52': '威海', '53': '温州', '54': '新乡',
             '55': '新余', '56': '宿州', '57': '徐州', '58': '烟台', '59': '盐城', '60': '扬州', '61': '阳江', '62': '阳泉', '63': '宜昌',
             '64': '宜春', '65': '鹰潭', '66': '岳阳', '67': '运城', '68': '枣庄', '69': '湛江', '70': '长治', '1024': '宝鸡',
             '1033': '许昌', '1032': '西宁', '1031': '渭南', '1030': '临沂', '1029': '莱芜', '1028': '景德镇', '1027': '呼和浩特',
             '1026': '东营', '1025': '本溪', '0': '白银', '47': '石嘴山', '4': '常熟', '2': '北京', '14': '海口', '73': '奉化',
             '79': '西安', '138': '龙岩', '147': '延吉', '99': '安阳', '103': '沧州', '95': '潍坊', '146': '达州', '74': '南京',
             '94': '珠海', '78': '武汉', '143': '丽水', '149': '安顺', '150': '贵港', '88': '南宁', '89': '南通', '155': '庆阳',
             '153': '漯河', '106': '阜新', '101': '保定', '98': '安庆', '83': '福州', '72': '大连', '160': '广州', '161': '苏州',
             '162': '天津', '163': '无锡', '164': '余姚', '165': '重庆', '166': '常州', '167': '哈尔滨', '168': '合肥', '169': '济南',
             '170': '乐清', '171': '乌鲁木齐', '172': '义乌', '173': '长春', '174': '郑州', '175': '洛阳', '176': '嘉兴', '177': '鞍山',
             '178': '北海', '179': '赤峰', '180': '德州', '181': '衡阳', '182': '淮北', '183': '吉林', '184': '廊坊', '185': '丽江',
             '186': '六安', '187': '茂名', '188': '莆田', '190': '齐齐哈尔', '191': '衢州', '192': '曲靖', '193': '三亚', '194': '韶关',
             '195': '唐山', '196': '铜川', '197': '宣城', '198': '漳州', '199': '中山', '200': '舟山', '201': '株洲', '202': '资阳',
             '203': '赣州', '204': '遵义', '205': '绍兴', '206': '包头', '207': '芜湖', '208': '银川', '209': '淮安', '210': '宜宾',
             '211': '张家口', '212': '肇庆', '213': '黄石', '214': '南阳', '215': '钦州', '216': '衡水', '217': '延边', '218': '云浮',
             '219': '内江', '220': '鄂州', '221': '鹤壁', '222': '雅安', '223': '仙桃', '121': '通化'}

city_index = {'百色': '1', '毕节': '3', '成都': '5', '池州': '6', '滁州': '7', '慈溪': '8', '东莞': '9', '佛山': '10', '抚州': '11',
              '广安': '12', '贵阳': '13', '上海': '42', '杭州': '15', '河池': '16', '河源': '17', '菏泽': '18', '湖州': '19',
              '怀化': '20',
              '惠州': '21', '济宁': '22', '揭阳': '23', '荆门': '24', '九江': '25', '昆明': '26', '兰州': '27', '六盘水': '28',
              '娄底': '29', '梅州': '30', '南昌': '31', '南平': '32', '宁波': '33', '宁德': '34', '宁海': '35', '平顶山': '36',
              '青岛': '37', '清远': '38', '泉州': '39', '厦门': '40', '汕头': '41', '石家庄': '46', '上饶': '43', '深圳': '44',
              '沈阳': '45', '镇江': '71', '台州': '48', '太原': '49', '泰安': '50', '铜陵': '51', '威海': '52', '温州': '53',
              '新乡': '54',
              '新余': '55', '宿州': '56', '徐州': '57', '烟台': '58', '盐城': '59', '扬州': '60', '阳江': '61', '阳泉': '62',
              '宜昌': '63',
              '宜春': '64', '鹰潭': '65', '岳阳': '66', '运城': '67', '枣庄': '68', '湛江': '69', '长治': '70', '宝鸡': '1024',
              '许昌': '1033', '西宁': '1032', '渭南': '1031', '临沂': '1030', '莱芜': '1029', '景德镇': '1028', '呼和浩特': '1027',
              '东营': '1026', '本溪': '1025', '白银': '0', '石嘴山': '47', '常熟': '4', '北京': '2', '海口': '14', '奉化': '73',
              '西安': '79', '龙岩': '138', '延吉': '147', '安阳': '99', '沧州': '103', '潍坊': '95', '达州': '146', '南京': '74',
              '珠海': '94', '武汉': '78', '丽水': '143', '安顺': '149', '贵港': '150', '南宁': '88', '南通': '89', '庆阳': '155',
              '漯河': '153', '阜新': '106', '保定': '101', '安庆': '98', '福州': '83', '大连': '72', '广州': '160', '苏州': '161',
              '天津': '162', '无锡': '163', '余姚': '164', '重庆': '165', '常州': '166', '哈尔滨': '167', '合肥': '168', '济南': '169',
              '乐清': '170', '乌鲁木齐': '171', '义乌': '172', '长春': '173', '郑州': '174', '洛阳': '175', '嘉兴': '176', '鞍山': '177',
              '北海': '178', '赤峰': '179', '德州': '180', '衡阳': '181', '淮北': '182', '吉林': '183', '廊坊': '184', '丽江': '185',
              '六安': '186', '茂名': '187', '莆田': '188', '齐齐哈尔': '190', '衢州': '191', '曲靖': '192', '三亚': '193', '韶关': '194',
              '唐山': '195', '铜川': '196', '宣城': '197', '漳州': '198', '中山': '199', '舟山': '200', '株洲': '201', '资阳': '202',
              '赣州': '203', '遵义': '204', '绍兴': '205', '包头': '206', '芜湖': '207', '银川': '208', '淮安': '209', '宜宾': '210',
              '张家口': '211', '肇庆': '212', '黄石': '213', '南阳': '214', '钦州': '215', '衡水': '216', '延边': '217', '云浮': '218',
              '内江': '219', '鄂州': '220', '鹤壁': '221', '雅安': '222', '仙桃': '223', '121': '通化'}

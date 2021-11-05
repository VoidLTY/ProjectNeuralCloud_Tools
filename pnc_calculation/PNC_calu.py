import pulp as lp
# 资源转换途径
recipe = {
    '开始游戏':{'游戏日':-1,'签到日':1,'日常日':1,'周常日':1,'免费通行证日':1,'付费通行证日':1,'宿舍日':1,'基建日':1,'作战日':1,'助战商店日':1,'体力':12*24-50,'好感':240,'标准商店日':2},
    '每日任务':{'日常日':-1,'好感':100,'基础检索指令':1,'底格币':3000,'经验':1400,'体力':100},
    '每周任务':{'周常日':-7,'好感':575,'基础检索指令':3,'体力':100,'底格币':5000,'经验':1800,'算法效率':360},
    '每月签到':{'签到日':-30,'好感':315,'底格币':35500,'经验':12500,'技能样本':300,'基础检索指令':2,'算法效率':220},
#通行证部分，付费的话就把付费部分的注释取消
    '免费通行证':{
        '免费通行证日':-35,'底格币':15000,'技能样本':2500,'紫突破':40,'蓝突破':20,'绿突破':20,'白突破':20,
        '经验':32000,'体力':250,'算法效率':500,'好感':250,'技能枢核':5
    },

    #'付费通行证':{
    #    '付费通行证日':-35,'底格币':50000,'技能样本':10000,
    #    '经验':168000,'体力':800,'算法效率':5000,'好感':625,'技能枢核':20,'金突破':10
    #},

#绿洲与宿舍部分，绿洲按全满级，宿舍按8级计算
    
    '基建':{'基建日':-1,'底格币':500*4*24*1.05,'预制件':1500,'基础检索指令':24*0.8,'通用工时':24+16,'指令工时':24,'礼物工时':24,'数据工时':24},
    '宿舍生产':{'宿舍日':-1,'通用工时':3,'经验':300},
    
#加工厂部分
    
    '预制件生产':{'通用工时':-1,'预制件':25},
    '加速指令':{'通用工时':-1,'指令工时':1},
    '加速礼物':{'通用工时':-1,'礼物工时':1},
    '加速数据':{'通用工时':-1,'数据工时':1},
    '指令生产':{'指令工时':-1,'基础检索指令':60/72.5},
    '模块生产':{'指令工时':-1,'预制件':-2000,'算法效率':2000,'算法碎片':-200},
    '模块生产(空转)':{'指令工时':-1,'算法效率':100/4.05,'算法碎片':-10/4.05},
    '礼物生产':{'礼物工时':-1,'好感':20},
    '枢核生产':{'数据工时':-1,'预制件':-300/8,'技能枢核':1/8},
    '枢核生产(空转)':{'数据工时':-1,'技能枢核':1/20},
    '技能箱生产':{'数据工时':-1,'预制件':-100/2,'底格币':-6000/2,'技能枢核':0.106/2,'技能样本':173.4/2},
    '技能箱生产(空转)':{'数据工时':-1,'底格币':-6000/6,'技能枢核':0.106/6,'技能样本':173.4/6},
    
#材料收集与算法本部分
    
    '双倍机会':{'作战日':-7,'双倍经验本门票':6,'双倍金币本门票':6,'双倍技能本门票':6,'双倍突破本门票':10},
    '双倍经验本':{'双倍经验本门票':-1,'体力':-30,'好感':64,'经验':18000},
    '双倍金币本':{'双倍金币本门票':-1,'体力':-30,'好感':64,'底格币':18000},
    '双倍技能本':{'双倍技能本门票':-1,'体力':-30,'好感':64,'技能样本':1560},
    '双倍突破本':{'双倍突破本门票':-1,'体力':-30,'好感':64,'金突破':5,'紫突破':5,'蓝突破':3,'绿突破':4,'白突破':4},
    '经验本':{'体力':-30,'好感':64,'经验':9000},
    '金币本':{'体力':-30,'好感':64,'底格币':9000},
    '技能本':{'体力':-30,'好感':64,'技能样本':780},
    '突破本':{'体力':-30,'好感':64,'金突破':5/2,'紫突破':5/2,'蓝突破':3/2,'绿突破':4/2,'白突破':4/2},
    '刷枢核':{'体力':-12.5,'技能枢核':1},
    '算法本':{'体力':-30,'好感':64,'蓝算法':2.0,'紫算法':1.0,'紫套装':1.9,'金算法':0.7},

#算法养成部分

    '吃蓝算法':{'蓝算法':-1,'算法效率':3},
    '吃紫算法':{'紫算法':-1,'算法效率':7},
    '拆紫算法':{'紫算法':-1,'算法碎片':2,'底格币':200},
    '吃紫套装':{'紫套装':-1,'算法效率':15},
    '拆紫套装':{'紫套装':-1,'算法碎片':2,'底格币':200},
    '吃金算法':{'金算法':-1,'算法效率':13},
    '拆金算法':{'金算法':-1,'算法碎片':7,'底格币':500},

#商店部分
    
    #'买高级算法模块':{'底格币':-8750,'算法效率':100,'标准商店日':-1},
    #'买经验':{'底格币':-3600,'经验':3600,'标准商店日':-1},
    '助战商店（买经验）':{'助战商店日':-7,'技能枢核':3,'经验':(200*7-740)*30},
    '助战商店（买底格币）':{'助战商店日':-7,'技能枢核':3,'底格币':(200*7-740)*30},
    '基础检索':{
        '基础检索指令':-1,
        '指令工时':85*2/60/1500,'礼物工时':15*6/60/1500+61*4/60/1500*1/3,'数据工时':61*4/60/1500*2/3,
        '经验':229900/1500,'好感':14565/1500,
        '金突破':83/1500,'紫突破':151/1500,'蓝突破':90/1500,'绿突破':79/1500,'白突破':46/1500,
    },

#人形养成部分，开放新上限不用改
    '人形养成':{
        '养成角色':1,'经验':-213540,'底格币':-129500,'技能样本':-23240,'技能枢核':-48,'好感':-13570,'算法效率':-6900,
        '金突破':-30,'紫突破':-40,'蓝突破':-30,'绿突破':-20,'白突破':-10,
    },
}

# 各项收支公式
var = {}
count = {}
for v, r in recipe.items():
    var[v] = lp.LpVariable(v,0)
    for i, c in r.items():
        count.setdefault(i,0)
        count[i] += c*var[v]

# 定义问题
problem = lp.LpProblem('养成计算',lp.LpMaximize)
count['游戏日'] += 30  #计算周期30天
for k, v in count.items():
    problem += v>=0,k
#方法1：强制规定养成角色数
#count['养成角色'] -= 4
#problem += var['算法本']*3+var['基础检索']

#方法2：利用权重控制养成角色数
problem += var['人形养成']*210+var['算法本']*3+var['基础检索']

#不想溢出资源可以取消下面的注释，但是会更亏一点
#problem += count['预制件']<=100
#problem += count['底格币']<=100

# 求解
if problem.solve() == 1:
    print('人形养成',var['人形养成'].value(),sep='\t')
    print('基础检索',var['基础检索'].value(),sep='\t')
    print('算法本',var['算法本'].value(),sep='\t')
    print('==========操作次数===========')
    #输出每种操作次数
    for k, v in var.items():
        if v.value()>0.001:
            print(k, v.value(),sep='\t')
    print('==========剩余库存===========')
    #输出库存
    for k, v in count.items():
        #print(k, problem.constraints[k].pi/problem.constraints['体力'].pi,sep='\t')
        if v.value()>0.001:
            print(k, v.value(),sep='\t')
else:
    print('unsolvable')
    

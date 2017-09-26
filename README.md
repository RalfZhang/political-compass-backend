# An Django Projcet

zuobiao.me 内容与分析后端接口

**Developing...**

## 接口列表

### 问题 questions

接口入口  
api/v1/


1. 获取所有问题  
/questions/  
GET
```json
[
    {
        "id": 1,
        "content": "如果人民没有受过民主教育，他们是不应该拥有普选权的。",
        "order_id": 101,
        "question_type": 1,
        "q_id": "q101",
        "rev": -1,
        "short": "普选权"
    },
    {
        "id": 2,
        "content": "人权高于主权。",
        "order_id": 102,
        "question_type": 1,
        "q_id": "q102",
        "rev": 1,
        "short": "人权与主权"
    },
    // ...
]
```

2. 获取单个问题详情  
/questions/{id}/  
GET  
```json
{
    "id": 23,
    "content": "在重大工程项目的决策中，个人利益应该为社会利益让路。",
    "order_id": 303,
    "question_type": 3,
    "q_id": "q303",
    "rev": -1,
    "short": "集体利益优先"
}
```

### 回答 answer

1. 添加回答  
/answers/  
POST  
字段： 'time', 'q101', 'q102', 'q104', 'q103', 'q106', 'q105', 'q107', 'q108', 'q109', 'q111', 'q110', 'q112', 'q113', 'q114', 'q115', 'q117', 'q119', 'q116', 'q120', 'q118', 'q301', 'q302', 'q303', 'q304', 'q305', 'q306', 'q309', 'q307', 'q308', 'q310', 'q311', 'q312', 'q313', 'q314', 'q316', 'q317', 'q318', 'q319', 'q320', 'q315', 'q201', 'q202', 'q203', 'q204', 'q205', 'q206', 'q207', 'q208', 'q209', 'q210', 'q1001', 'q1002', 'q1003', 'q1004', 'ip', 'device', 'add'


### 统计 stats

1. 获取单个问题回答的分布  
/stats/question_distribution?id=''
问题选项数量，比例，均分，和方差

2. 获取总体分布  
/stats/compass_distribution?type=1

3. 以一个问题选项分类三个坐标平均值  
/stats/compass_distribution_by_question

4. 以一个问题选项分类所有问题回答均值  
/stats/question_distribution_by_question 

### 分析 analyse

1. 获取两个问题相关性  
/analyse/dependent?ids=[1,2]  

2. 获取坐标相关性  
(?)
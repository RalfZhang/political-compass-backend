# An Django Projcet

zuobiao.me 内容与分析后端接口

**Developing...**

## 接口列表

### 问题 questions

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
1. 获取所有回答  
/answers/
GET
```json
```
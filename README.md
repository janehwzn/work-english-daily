# Work English Daily · 职场英语每日一练

每天一个工作场景，15 分钟开口练习。从每日邮件开始，长成一个订阅制英语练习产品。

## 这是什么

- **每日场景**：每天早上一个工作场景（standup / sprint planning / grooming / small talk / 1:1 / 周末复习），
  带完整对话脚本（英文 + 中文注释 + 发音提示）、金句、15 分钟练习法和角色扮演挑战。
- **练习 App**：打开 App 就是今日场景——跟读（TTS）、背诵、打卡，连续打卡记 streak。
- **场景库**：`scenarios/` 下每个场景一个 JSON，可搜索、可按分类浏览。

## 目录结构

```
work-english-daily/
├── README.md               # 本文件
├── SUBSCRIPTION.md         # 订阅制产品路线图
├── docs/
│   └── SCHEMA.md           # 场景 JSON 字段规范
├── scenarios/
│   ├── index.json          # 场景清单（构建脚本生成）
│   ├── standup.json
│   ├── sprint-planning.json
│   └── ...                 # 每个场景一个文件
└── scripts/
    └── build_index.py      # 生成 scenarios/index.json
```

## 每日轮换（和邮件版保持一致）

| 周几 | 场景 |
|------|------|
| Mon | Daily standup |
| Tue | Sprint planning |
| Wed | Backlog grooming |
| Thu | Small talk（会前闲聊） |
| Fri | 1:1 with manager |
| Sat/Sun | 周末轻量复习 |

其余场景在 App 的题库里随时可练。

## 本地预览场景数据

```bash
python3 scripts/build_index.py   # 重新生成 scenarios/index.json
```

## Roadmap

更多场景持续更新中，Pro 版本即将上线，敬请期待。

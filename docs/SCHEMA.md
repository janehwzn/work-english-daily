# Scenario JSON Schema

每个场景是一个 JSON 文件，放在 `scenarios/<id>.json`。App 启动时会打包这些文件。

## 字段

```json
{
  "id": "standup",
  "title": "Daily Standup",
  "title_zh": "每日站会",
  "category": "scrum",
  "category_zh": "敏捷会议",
  "weekdays": ["Mon"],
  "tier": "free",
  "scene_zh": "中文 2-3 句：这个场景什么时候出现、跟谁说、这次对话的目标是什么。",
  "dialogue": [
    {
      "speaker": "You",
      "en": "Yesterday I finished the Storm 2 migration for the Drova pipeline.",
      "zh": "昨天我完成了 Drova pipeline 的 Storm 2 迁移。",
      "tip": "finished 的 -ed 和 the 连读时轻读，重音在 migration"
    }
  ],
  "key_phrases": [
    {
      "en": "No blockers on my end.",
      "zh": "我这边没有阻塞。",
      "note": "比 I don't have blockers 更地道"
    }
  ],
  "practice_zh": [
    "跟读 5 分钟：打开 TTS 朗读，每句跟读 2 遍，注意连读和重音",
    "背诵 5 分钟：遮住英文，只看中文说出英文",
    "角色扮演 5 分钟：把对话里的项目换成你自己的真实进展，大声说一遍"
  ],
  "roleplay_zh": "你是今天 standup 的发言人，用三句话讲你的 Storm 迁移进展：昨天做了什么、今天做什么、有没有 blocker。",
  "check_in_zh": "今天练了吗？点 App 里的打卡按钮 ✅"
}
```

## 规范

- `id`：kebab-case，文件名同名。
- `category` 取值：`scrum` / `small-talk` / `one-on-one` / `meeting` / `review`。
- `weekdays`：该场景固定出现在周几（与每日邮件轮换一致）。只能用以下映射，
  其他场景设为 `[]`：
  - Mon: standup；Tue: sprint-planning；Wed: backlog-grooming；
  - Thu: small-talk-meeting-opener；Fri: one-on-one-manager-update；
  - Sat/Sun: weekend-review
- `tier`：一律 `"free"`（以后做订阅时再分层，字段先留好）。
- `dialogue`：8–14 个 turn。`speaker` 用 `You` 表示用户，其他角色用英文名
  （如 Maya、Tom、Alex）。`en` 必须是自然口语（不要教科书腔）；
  `zh` 是中文注释；`tip` 可选（发音/连读/语调提示，中文写）。
- 内容贴合用户画像：Salesforce Lead MTS，做 Storm 1→2 迁移 + Drova 数据 pipeline，
  团队是 network engineers。技术场景里可以用她的真实工作内容。
- `key_phrases`：4–6 条，可直接套用的句子，配中文和一句使用说明。
- `practice_zh`：3 步，正好 15 分钟。
- JSON 内容里不要出现 emoji（App 负责样式）。
- 文件必须是合法 JSON，UTF-8。

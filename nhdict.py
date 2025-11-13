#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetHack English‑Chinese Dictionary CLI
=====================================

This script provides a simple command‑line interface to translate common
NetHack terms from English to Chinese.  It contains a built‑in dictionary
covering status fields, actions, monsters, items, terrain, status effects
and specialized NetHack terminology.  The lookup is case‑insensitive and
supports multi‑word phrases (e.g. ``"scroll of teleportation"``).

Usage::

    python nhdict.py <term>

For example::

    python nhdict.py goblin
    python nhdict.py "scroll of enchant armor"

If no term is provided or the term is not found in the dictionary, a
help message is displayed.  Feel free to extend the ``DICT`` mapping
with additional words or phrases as you encounter them in the game.
"""
import sys


#: Mapping of English terms (lower‑case) to Chinese translations.
DICT = {
    # Status/Stats
    "hp": "生命值",
    "max hp": "最大生命值",
    "pw": "法力值 / 魔力",
    "power": "法力值 / 魔力",
    "ac": "护甲等级（越低越好）",
    "level": "等级",
    "xp": "经验值",
    "str": "力量",
    "dex": "敏捷",
    "con": "体质",
    "int": "智力",
    "wis": "愿力 / 感知",
    "cha": "魅力",
    "hunger": "饥饿值",
    "encumbrance": "负重",
    "satiated": "撑",
    "hungry": "饥饿",
    "weak": "虚弱",
    "fainting": "昏厥",

    # Actions/Commands
    "move": "移动",
    "kick": "踢",
    "eat": "吃",
    "wield": "装备（武器）",
    "wear": "穿戴（护甲）",
    "put on": "戴上（戒指、护符）",
    "remove": "移除",
    "drop": "扔下",
    "throw": "投掷",
    "zap": "使用魔杖",
    "engrave": "刻字（常用于写“Elbereth”防身）",
    "search": "搜索",
    "open": "打开门",
    "close": "关门",
    "quaff": "喝（药水）",
    "read": "阅读（卷轴/书）",
    "pray": "祈祷",
    "sacrifice": "祭品",
    "offer": "献祭尸体在祭坛",
    "rest": "休息",

    # Monsters
    "goblin": "哥布林",
    "kobold": "科博德",
    "orc": "兽人",
    "troll": "巨魔",
    "dwarf": "矮人",
    "giant": "巨人",
    "dragon": "龙",
    "mummy": "木乃伊",
    "vampire": "吸血鬼",
    "lich": "巫妖",
    "demon": "恶魔",
    "angel": "天使",
    "minotaur": "米诺陶牛头怪",
    "bat": "蝙蝠",
    "floating eye": "浮空眼",
    "gelatinous cube": "史莱姆方块",
    "mimic": "拟态怪",
    "golem": "魔像",
    "zombie": "僵尸",
    "werewolf": "狼人",

    # Weapons
    "dagger": "匕首",
    "sword": "剑",
    "long sword": "长剑",
    "two‑handed sword": "双手剑",
    "mace": "钉锤",
    "spear": "矛",
    "bow": "弓",
    "arrow": "箭",
    "crossbow": "弩",
    "wand": "魔杖",

    # Armor
    "helmet": "头盔",
    "boots": "靴子",
    "cloak": "斗篷",
    "shield": "盾牌",
    "body armor": "身甲",
    "gloves": "手套",

    # Rings
    "ring of protection": "防御戒指",
    "ring of polymorph": "变形戒指",
    "ring of teleport control": "传送控制戒指",
    "ring of fire resistance": "防火戒指",
    "ring of slow digestion": "缓慢消化戒指",

    # Scrolls
    "scroll of identify": "鉴定卷轴",
    "scroll of teleportation": "传送卷轴",
    "scroll of enchant weapon": "强化武器卷轴",
    "scroll of enchant armor": "强化护甲卷轴",
    "scroll of remove curse": "祛除诅咒卷轴",
    "scroll of magic mapping": "魔法地图卷轴",

    # Potions
    "potion of healing": "治疗药水",
    "potion of full healing": "完全治疗药水",
    "potion of invisibility": "隐形药水",
    "potion of levitation": "漂浮药水",
    "potion of gain level": "升级药水",
    "potion of paralysis": "麻痹药水",

    # Wands
    "wand of fire": "火焰魔杖",
    "wand of cold": "冰霜魔杖",
    "wand of lightning": "闪电魔杖",
    "wand of teleportation": "传送魔杖",
    "wand of digging": "挖掘魔杖",
    "wand of wishing": "许愿魔杖（最强）",

    # Dungeon terrain
    "altar": "祭坛",
    "shop": "商店",
    "fountain": "喷泉",
    "sink": "水槽",
    "trap": "陷阱",
    "stairs": "楼梯",
    "up staircase": "上楼梯",
    "down staircase": "下楼梯",
    "vault": "宝库",
    "corridor": "走廊",

    # Status effects
    "blessed": "祝福",
    "cursed": "诅咒",
    "uncursed": "未诅咒",
    "confused": "混乱",
    "blind": "失明",
    "stunned": "眩晕",
    "hallucinating": "幻觉",
    "poisoned": "中毒",
    "sick": "生病",
    "sleep": "睡眠",
    "paralysis": "麻痹",
    "deaf": "失聪",
    "invisible": "隐形",

    # Special NetHack terms
    "elbereth": "保护用刻字（能吓跑怪）",
    "conduct": "禁忌挑战（如素食、无杀生）",
    "ascension": "通关（成功携物品离开世界）",
    "yasd": "非常蠢的死法",
    "enlightenment": "角色状态展示界面",
    "polypiling": "用“变形+堆叠”刷神器",
    "sokoban": "推箱子支线",
    "gehennom": "地狱区域",
    "quest": "职业任务线",
}


def lookup(term: str) -> str:
    """Return the Chinese translation for the given English ``term``.

    The lookup is case‑insensitive and returns ``None`` if the term is not
    present in the dictionary.
    """
    key = term.lower().strip()
    return DICT.get(key)


def main(argv: list[str]) -> None:
    if not argv:
        print("Usage: python nhdict.py <English term or phrase>")
        print("Example: python nhdict.py \"scroll of teleportation\"")
        print("Translations are case‑insensitive and spaces matter.")
        return
    # Join arguments to support multi‑word phrases
    term = " ".join(argv)
    translation = lookup(term)
    if translation:
        print(f"{term} -> {translation}")
    else:
        print(f"No translation found for: {term}")


if __name__ == "__main__":
    main(sys.argv[1:])
#!/usr/bin/env python3
"""读者导航的稳定分类、标题译名和排序规则。

归档文件路径是事实层，不因阅读体验调整而移动。这个模块只负责在索引层提供：

- 稳定、可读的主题 slug；
- 中文优先的展示状态和排序；
- 未译英文博客的目录标题译名；
- 明显不是文章的归档噪声过滤。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


TITLE_ALIASES_REL = Path("meta/blog_title_aliases.json")


@dataclass(frozen=True)
class TopicSpec:
    slug: str
    name: str
    description: str
    core: bool = True


TOPIC_SPECS: tuple[TopicSpec, ...] = (
    TopicSpec(
        "objective-c-runtime",
        "Objective-C Runtime",
        "对象模型、消息发送、方法解析、转发、关联对象与运行时机制。",
    ),
    TopicSpec(
        "memory-arc",
        "内存与 ARC",
        "引用计数、所有权、autorelease、weak、指针、内存布局与泄漏。",
    ),
    TopicSpec(
        "blocks-closures",
        "Block 与闭包",
        "Block ABI、捕获语义、逃逸闭包、回调和函数指针。",
    ),
    TopicSpec(
        "runloop-responsiveness",
        "RunLoop 与响应性",
        "RunLoop、事件循环、Timer、卡顿、挂起和主线程响应性。",
    ),
    TopicSpec(
        "concurrency",
        "并发与线程",
        "GCD、Operation、锁、原子操作、数据竞争、Actor 与 Swift 并发。",
    ),
    TopicSpec(
        "performance-debugging",
        "性能与调试",
        "Instruments、LLDB、崩溃、Sanitizer、性能分析和诊断。",
    ),
    TopicSpec(
        "launch-linking-binary",
        "启动、链接与二进制",
        "App 启动、dyld、Mach-O、编译器、链接器、动态库和二进制体积。",
    ),
    TopicSpec(
        "ui-rendering",
        "UI 与渲染",
        "UIKit、SwiftUI、事件、动画、Core Graphics、Core Animation 与 Metal。",
    ),
    TopicSpec(
        "network-security",
        "网络与安全",
        "HTTP、TCP、TLS、证书、Keychain、密码学和网络诊断。",
    ),
    TopicSpec(
        "data-persistence",
        "数据与持久化",
        "Core Data、SwiftData、数据库、文件、序列化和持久化。",
    ),
    TopicSpec(
        "swift-language",
        "Swift 语言",
        "类型系统、泛型、协议、值语义、宏和语言演进。",
        core=False,
    ),
    TopicSpec(
        "architecture-testing",
        "架构、测试与工程实践",
        "架构、测试、依赖管理、模块化、CI 和工程工作流。",
        core=False,
    ),
)

TOPIC_BY_NAME = {topic.name: topic for topic in TOPIC_SPECS}


SUBTOPIC_RULES: dict[str, tuple[tuple[str, str], ...]] = {
    "Objective-C Runtime": (
        ("对象、类与 isa", r"\bisa\b|class object|metaclass|object model|non-pointer"),
        ("消息发送与转发", r"objc_msgsend|message|forward|invocation|selector"),
        ("动态能力", r"swizzl|associated object|method resolution|\bkvo\b|runtime"),
    ),
    "内存与 ARC": (
        ("ARC 与引用计数", r"\barc\b|reference count|retain|release|\bweak\b|ownership"),
        ("Autorelease", r"autorelease|autoreleasing"),
        ("指针与内存布局", r"pointer|memory layout|\bstack\b|\bheap\b|\bvmmap\b"),
        ("分配与泄漏", r"allocat|\bmalloc\b|\bleak\b|memory graph"),
    ),
    "Block 与闭包": (
        ("Block ABI 与实现", r"\bblocks?\b|block abi|block object"),
        ("捕获与生命周期", r"capture|escaping|retain cycle|lifetime"),
        ("闭包与函数指针", r"closures?|function pointer|callback"),
    ),
    "RunLoop 与响应性": (
        ("RunLoop 与 Timer", r"run\s*loop|runloop|\btimer\b|event loop"),
        ("卡顿与挂起", r"\bhitches?\b|\bhangs?\b|responsiveness|stall"),
        ("显示循环", r"display\s*link|render loop|frame"),
    ),
    "并发与线程": (
        ("GCD 与 Operation", r"\bgcd\b|grand central dispatch|\bdispatch\b|operation"),
        ("锁与原子操作", r"\blocks?\b|\bmutex\b|semaphore|atomic|os_unfair"),
        ("Swift 并发", r"async|await|\bactors?\b|sendable|task group"),
        ("数据竞争与线程安全", r"data race|thread safe|race condition|\bthreads?\b"),
    ),
    "性能与调试": (
        ("Instruments 与性能分析", r"instruments|profil|performance|benchmark|metric"),
        ("LLDB 与调试", r"\blldb\b|\bdebug|breakpoint"),
        ("崩溃与符号化", r"\bcrash|symbolicat|stack trace|unwind"),
        ("Sanitizer 与诊断", r"sanitizer|diagnos|memory graph|c-reduce|fuzz"),
    ),
    "启动、链接与二进制": (
        ("App 启动与 dyld", r"\blaunch|\bdyld\b|load time|prewarm"),
        ("Mach-O 与链接器", r"mach-o|\blinkers?\b|\blinking\b|relocation|symbol"),
        ("编译与构建", r"compil|build system|xcode build|llvm"),
        ("动态库与体积", r"dylib|dynamic librar|framework|app size|binary size"),
    ),
    "UI 与渲染": (
        ("UIKit 与事件", r"\buikit\b|touch|gesture|responder|view controller"),
        ("SwiftUI", r"\bswiftui\b"),
        ("动画与渲染循环", r"animation|render loop|display link|frame rate"),
        ("图形与 GPU", r"core graphics|core animation|\bmetal\b|gpu|texture|graphics"),
    ),
    "网络与安全": (
        ("网络与 HTTP", r"\bnetwork|\bhttp|urlsession|\bsocket|\btcp\b"),
        ("TLS 与证书", r"\btls\b|\bssl\b|certificate|trust"),
        ("Keychain 与密码学", r"keychain|crypt|signing|encryption"),
        ("认证与网络诊断", r"authentication|authorization|diagnos|metrics"),
    ),
    "数据与持久化": (
        ("Core Data", r"core data|nsmanaged|persistent store"),
        ("SwiftData", r"swiftdata|modelcontainer|modelcontext"),
        ("数据库与文件", r"\bdatabase|\bsqlite\b|file system|storage"),
        ("序列化", r"\bjson\b|serialization|archive|codable"),
    ),
}


NOISE_EXACT = {
    "",
    "(see all tags)",
    "articles",
    "archive",
    "archives",
    "archive",
    "about",
    "categories",
    "contact",
    "feed",
    "home",
    "index",
    "next",
    "posts",
    "previous",
    "rss",
    "tags",
    "onev’s den",
}
NOISE_PATTERNS = (
    re.compile(r"^posts from \d{4}$", re.I),
    re.compile(
        r"^(january|february|march|april|may|june|july|august|september|"
        r"october|november|december)\s+\d{4}$",
        re.I,
    ),
    re.compile(r"^(?:define|include)\s+[A-Z_(),\s]+$"),
)


def is_reader_visible_title(title: str, source_url: str = "") -> bool:
    """排除明显的归档入口、月份页和误抓成标题的预处理器片段。"""
    normalized = re.sub(r"\s+", " ", title).strip()
    if normalized.casefold() in NOISE_EXACT:
        return False
    if re.search(r"/(?:page\d*|tags?|categories|archives?)/?$", source_url, re.I):
        return False
    return not any(pattern.search(normalized) for pattern in NOISE_PATTERNS)


def has_han(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def topic_slug(topic_name: str) -> str:
    spec = TOPIC_BY_NAME.get(topic_name)
    if spec is None:
        raise KeyError(f"未登记的主题：{topic_name}")
    return spec.slug


def classify_subtopic(topic_name: str, text: str) -> str:
    """在一级主题内给出一个稳定子主题；无法可靠判断时回到“其他”。"""
    for name, pattern in SUBTOPIC_RULES.get(topic_name, ()):
        if re.search(pattern, text, re.I):
            return name
    return "其他"


def load_title_aliases(root: Path) -> dict[str, dict[str, str]]:
    path = root / TITLE_ALIASES_REL
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") != 1 or not isinstance(data.get("titles"), dict):
        raise ValueError(f"标题译名文件格式错误：{path}")
    result: dict[str, dict[str, str]] = {}
    for rel, value in data["titles"].items():
        if not isinstance(value, dict):
            raise ValueError(f"标题译名条目不是对象：{rel}")
        en_title = str(value.get("en_title") or "").strip()
        zh_title = str(value.get("zh_title") or "").strip()
        if not en_title or not zh_title or "\n" in zh_title:
            raise ValueError(f"标题译名条目不完整：{rel}")
        result[str(rel)] = {"en_title": en_title, "zh_title": zh_title}
    return result


def title_alias_for(
    en_path: Path | None,
    *,
    root: Path,
    aliases: dict[str, dict[str, str]],
    current_title: str,
) -> str:
    if en_path is None:
        return ""
    try:
        rel = en_path.relative_to(root).as_posix()
    except ValueError:
        return ""
    record = aliases.get(rel)
    if not record:
        return ""
    if record["en_title"] != current_title:
        raise ValueError(
            f"目录标题译名已过期：{rel}，记录为 {record['en_title']!r}，"
            f"当前为 {current_title!r}"
        )
    return record["zh_title"]


def display_status(entry: dict[str, Any]) -> str:
    status = entry["status"]
    if status == "待翻译" and entry.get("title_alias"):
        return "仅标题中文，正文待翻译"
    return status


def status_rank(entry: dict[str, Any]) -> int:
    """完整中文优先，其次原生中文、仅标题中文、纯英文和归档噪声。"""
    if not entry.get("reader_visible", True):
        return 4
    status = entry["status"]
    if status == "已翻译":
        return 0
    if status == "原生中文":
        return 1
    if entry.get("title_alias"):
        return 2
    return 3


def preferred_title(entry: dict[str, Any]) -> str:
    zh_title = entry.get("zh_title") or ""
    alias = entry.get("title_alias") or ""
    if zh_title and has_han(zh_title):
        return zh_title
    return alias or zh_title or entry.get("en_title") or "未命名"


def needs_title_alias(entry: dict[str, Any]) -> bool:
    """正文待翻译，或已有中文正文但标题仍全英文时，需要目录译名。"""
    if not entry.get("en") or not entry.get("reader_visible", True):
        return False
    if entry["status"] == "待翻译":
        return True
    return entry["status"] == "已翻译" and not has_han(entry.get("zh_title") or "")

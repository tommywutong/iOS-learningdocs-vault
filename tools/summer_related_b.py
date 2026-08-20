#!/usr/bin/env python3
"""生成并核验暑期强相关 B 类翻译白名单。

    python3 tools/summer_related_b.py write
    python3 tools/summer_related_b.py check
    python3 tools/summer_related_b.py report

范围裁决见 meta/SUMMER_RELATED_B_PLAN.md。本工具只读取现有英文原文和译文状态，
不会调用模型、抓取网络或修改英文基线。
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indexes import display_title, read_fm  # noqa: E402
from shard import already_translated_elsewhere  # noqa: E402
from translate_plan import ROOT, collect  # noqa: E402

MANIFEST = ROOT / "meta" / "summer_related_b_allowlist.json"
APPROVED_ON = "2026-07-29"

APPLE_FRAMEWORKS = {
    "apple-silicon",
    "avfoundation",
    "cfnetwork",
    "combine",
    "coredata",
    "coregraphics",
    "coreimage",
    "cryptokit",
    "dispatch",
    "foundation",
    "imageio",
    "kernel",
    "metal",
    "metrickit",
    "network",
    "observation",
    "os",
    "quartzcore",
    "security",
    "swift",
    "swiftdata",
    "synchronization",
    "technotes",
    "technologyoverviews",
    "testing",
    "uikit",
    "xcode",
}

APPLE_TITLE_RULES = {
    "apple-silicon": r"performance|memory|debug",
    "avfoundation": (
        r"responsive camera app|loading media data asynchronously|"
        r"play and persist http live streams|fragmented mpeg-4"
    ),
    "combine": r"asynchronous code|timer publishers",
    "coredata": (
        r"core data stack|persistent history|persistent store types|conflict resolution|"
        r"batch processing|model migration|migrating your data model|staged migrations|"
        r"using core data in the background"
    ),
    "cryptokit": r"cryptographic operations|keys in the keychain",
    "dispatch": r".+",
    "foundation": r"^thread$|streams, sockets, and ports|task management|^xpc$",
    "kernel": r"atomic operations|memory|debugging",
    "metal": (
        r"memory|synchroni[sz]|display link|frame rates|render pass|rendering performance|"
        r"resource loading|dynamic librar|binary size|threads and threadgroups|gpu and the cpu"
    ),
    "metrickit": r".+",
    "network": (
        r"network debugging|network connection metrics|local network tls|https problems|"
        r"netcat|security options|tcp options|tls options"
    ),
    "observation": r".+",
    "os": r".+",
    "quartzcore": r"^core animation$|promotion displays",
    "security": (
        r"hardened runtime|launch environment|library constraints|certificate, key, and trust|"
        r"examining a certificate|using keys for encryption|secure socket layer|"
        r"preventing insecure network|working with concurrency|pointer authentication|"
        r"keychain items|keys in the keychain|secrets"
    ),
    "swift": (
        r"objective-c|strict concurrency|swift concurrency|pointer parameters|"
        r"failable asynchronous"
    ),
    "swiftdata": r"concurrency|persistent|migration|model",
    "synchronization": r".+",
    "technotes": r"code signing|memory|performance|network|launch",
    "technologyoverviews": r"testing and performance|networking and communication",
    "testing": r"asynchronous|performance",
    "uikit": (
        r"app launch sequence|responding to the launch|life cycle|gesture recognizer|"
        r"handling touches|touch input|predicted touches|target.action|"
        r"container view controller|view controller transitions|"
        r"high.performance lists|customizing drawings"
    ),
    "xcode": r"performance|debug|instruments|build|launch",
}

BLOG_SOURCES = {
    "alwaysprocessing",
    "belkadan",
    "ciechanowski",
    "cocoawithlove",
    "emergetools",
    "fbeng",
    "jessesquires",
    "lowlevelbits",
    "maskray",
    "mikeash",
    "nshipster",
    "oleb",
    "saagarjha",
    "worthdoingbadly",
}

THEME_RULES: tuple[tuple[str, str], ...] = (
    (
        "memory-runtime-blocks",
        r"objective[ -]?c|\bobjc\b|runtime|method swizz|message (?:send|dispatch|forward)|"
        r"selector|associated object|tagged pointer|\bisa\b|\bkvc\b|\bkvo\b|\bmemory\b|"
        r"\barc\b|retain|release|autorelease|\bweak\b|ownership|pointer|\bheap\b|\bstack\b|"
        r"allocat|\bleak|reference count|\bblocks?\b|\bclosures?\b|capture list",
    ),
    (
        "concurrency",
        r"concurren|\bthreads?\b|\bgcd\b|\bdispatch\b|\blocks?\b|mutex|semaphore|"
        r"data race|\bactors?\b|\basync\b|\bawait\b|sendable|atomic|synchroni[sz]|"
        r"operation queue|nsoperation",
    ),
    (
        "runloop-events-lifecycle",
        r"run\s*loop|runloop|event loop|responder|target.action|gesture recognizer|"
        r"\btouches?\b|touch input|life\s*cycle|lifecycle|app launch|launch sequence|"
        r"view controller transition|container view controller",
    ),
    (
        "rendering-performance",
        r"\brender|drawing|graphics|core animation|display link|frame rate|latency|"
        r"\bhitch|\bhang|scroll.*performance|high.performance (?:list|collection)|"
        r"image (?:decod|cach)|gpu memory|texture memory|render pass|pro.?motion",
    ),
    (
        "build-link-launch",
        r"mach.?o|\bdyld\b|linker|\blinking\b|dynamic librar|\bbinary|build time|"
        r"app size|startup|launch time|symbolicat|library constraint",
    ),
    (
        "debugging-observability",
        r"\bperformance\b|instruments|\blldb\b|\bdebug|\bcrash|profil|metric(?:kit)?|"
        r"memory graph|sanitizer|diagnos|logging",
    ),
    (
        "network-security",
        r"\btcp\b|\bhttp|\btls\b|\bssl\b|\bnetwork|certificate|keychain|crypt|"
        r"\bsocket|authentication|hardened runtime",
    ),
    (
        "data-persistence",
        r"\bsqlite\b|\bjson\b|protobuf|persist|core data|swiftdata|\bdatabase\b|"
        r"seriali[sz]|file system|store migration|persistent history|core data stack",
    ),
)

GENERIC_TITLE = re.compile(
    r"(?:Implementations|Constants|Data Types|Enumerations|Functions|Macros|Structures|"
    r"Error Codes|Result Codes|Property Keys|Attribute Constants|Deprecated Symbols|"
    r"Release Notes)$",
    re.IGNORECASE,
)

PATH_EXCLUDES = (
    "/updates/",
    "release-notes",
    "-async-properties.md",
    "/deprecated",
)

EXPLICIT_EXCLUDES = {
    "apple-docs/en/metal/implementing-order-independent-transparency-with-image-blocks.md",
    "apple-docs/en/quartzcore/emitter-render-order.md",
    "apple-docs/en/swift/tictacfish_implementing_a_game_using_distributed_actors.md",
    "blogs/en/cocoawithlove/finding-the-bounding-box-of-a-path-cocoa-with-love.md",
    "blogs/en/fbeng/how-meta-built-threads-in-5-months.md",
    "blogs/en/maskray/weak-avl-tree.md",
    "blogs/en/oleb/is-it-immoral-to-not-block-ads.md",
    "blogs/en/worthdoingbadly/volte-vowifi-research-with-0-of-equipment-set-up-a-phone-network-over-wi-fi-calling.md",
}

BLOG_OFF_TOPIC = re.compile(
    r"android|react conf|macbook|crashplan|python operator|wiring your house|"
    r"gene drive|gpu passthrough|qemu|black screen|kids' novel|phone network|"
    r"implicit.*atomic|weak avl|block ads|mail\\.app deep link|"
    r"co-experiences|analytics sdks|configuration profiles",
    re.IGNORECASE,
)

WWDC_OFF_TOPIC = re.compile(
    r"game's memory|driverkit|mac app|apple silicon mac|swiftui animation|"
    r"rich graphics to your swiftui|background tasks in swiftui|"
    r"what.s new in swiftdata",
    re.IGNORECASE,
)

SMOKE_FILES = (
    "apple-docs/en/uikit/about-the-app-launch-sequence.md",
    "wwdc/en/wwdc2023/10248-analyze-hangs-with-instruments.md",
    "blogs/en/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md",
)

EXPLICIT_INCLUDES = {
    "apple-docs/en/uikit/about-the-app-launch-sequence.md",
    "apple-docs/en/uikit/about-the-gesture-recognizer-state-machine.md",
    "apple-docs/en/uikit/building-high-performance-lists-and-collection-views.md",
    "apple-docs/en/uikit/managing-your-app-s-life-cycle.md",
    "apple-docs/en/uikit/minimizing-latency-with-predicted-touches.md",
    "apple-docs/en/uikit/responding-to-control-based-events-using-target-action.md",
    "apple-docs/en/swift/updating-an-app-to-use-strict-concurrency.md",
    "apple-docs/en/swift/using-objective-c-runtime-features-in-swift.md",
    "apple-docs/en/avfoundation/building-a-camera-app.md",
    "apple-docs/en/avfoundation/loading-media-data-asynchronously.md",
    "blogs/en/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md",
}


def themes_for(text: str) -> list[str]:
    return [
        name
        for name, pattern in THEME_RULES
        if re.search(pattern, text, re.IGNORECASE)
    ]


def apple_framework(rel: str) -> str:
    parts = Path(rel).parts
    return parts[2] if len(parts) > 2 else ""


def source_key(rel: str) -> str:
    parts = Path(rel).parts
    if rel.startswith("blogs/en/") and len(parts) > 2:
        return parts[2]
    if rel.startswith("apple-docs/en/"):
        return apple_framework(rel)
    if rel.startswith("wwdc/en/") and len(parts) > 2:
        return parts[2]
    return parts[0]


def candidate(item: dict) -> dict | None:
    rel = item["en"]
    if rel in EXPLICIT_EXCLUDES:
        return None
    path = ROOT / rel
    title = display_title(path, read_fm(path))
    if GENERIC_TITLE.search(title) or any(token in rel.casefold() for token in PATH_EXCLUDES):
        return None

    text = f"{title} {path.stem}"
    themes = themes_for(text)
    if rel in EXPLICIT_INCLUDES and not themes:
        themes = ["approved-explicit"]

    if item["source"] == "apple-docs":
        framework = apple_framework(rel)
        if framework not in APPLE_FRAMEWORKS:
            return None
        pattern = APPLE_TITLE_RULES.get(framework)
        if (
            not pattern
            or not re.search(pattern, title, re.IGNORECASE)
        ) and rel not in EXPLICIT_INCLUDES:
            return None
    elif item["source"] == "blogs":
        if source_key(rel) not in BLOG_SOURCES:
            return None
        if BLOG_OFF_TOPIC.search(title):
            return None
    elif item["source"] != "wwdc":
        return None
    elif WWDC_OFF_TOPIC.search(title):
        return None

    if not themes and rel not in EXPLICIT_INCLUDES:
        return None

    return {
        "en": rel,
        "zh": item["zh"],
        "source": item["source"],
        "source_key": source_key(rel),
        "title": title,
        "themes": themes,
        "chars": len(path.read_text(encoding="utf-8")),
    }


def build_manifest() -> dict:
    paired = already_translated_elsewhere()
    files = []
    for item in collect():
        if item["en"] in paired:
            continue
        selected = candidate(item)
        if selected:
            files.append(selected)
    theme_order = {name: i for i, (name, _) in enumerate(THEME_RULES)}
    files.sort(
        key=lambda x: (
            min((theme_order.get(t, 99) for t in x["themes"]), default=99),
            x["source"],
            x["source_key"],
            x["en"],
        )
    )
    return {
        "scope": "summer-related-b",
        "approved_on": APPROVED_ON,
        "plan": "meta/SUMMER_RELATED_B_PLAN.md",
        "file_count": len(files),
        "chars": sum(item["chars"] for item in files),
        "smoke_files": list(SMOKE_FILES),
        "files": files,
    }


def render(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def validate_frozen_manifest(data: dict) -> None:
    if data.get("scope") != "summer-related-b":
        raise SystemExit("B 类白名单 scope 不正确")
    files = data.get("files")
    if not isinstance(files, list) or len(files) != data.get("file_count"):
        raise SystemExit("B 类白名单文件数量不正确")
    paths = [str(item.get("en") or "") for item in files]
    if len(paths) != len(set(paths)):
        raise SystemExit("B 类白名单存在重复英文路径")
    if list(data.get("smoke_files") or []) != list(SMOKE_FILES):
        raise SystemExit("B 类冒烟文件与当前裁决不一致")
    if not set(SMOKE_FILES) <= set(paths):
        raise SystemExit("B 类冒烟文件不属于完整白名单")
    if sum(int(item.get("chars") or 0) for item in files) != data.get("chars"):
        raise SystemExit("B 类白名单字符总数不正确")
    for item in files:
        rel = str(item.get("en") or "")
        zh = str(item.get("zh") or "")
        expected = rel.replace("/en/", "/zh/", 1)
        if zh != expected:
            raise SystemExit(f"B 类中英路径不匹配：{rel} → {zh}")
        if not (ROOT / rel).is_file():
            raise SystemExit(f"B 类英文原文不存在：{rel}")
        if not item.get("themes"):
            raise SystemExit(f"B 类文档缺少主题：{rel}")
        reviewed = candidate(item)
        if reviewed is None:
            raise SystemExit(f"B 类文档不再符合当前筛选规则：{rel}")


def report(data: dict) -> None:
    print(f"B 类白名单：{data['file_count']} 篇 / {data['chars']:,} 字符")
    print("来源：")
    for name, count in Counter(f["source"] for f in data["files"]).most_common():
        chars = sum(f["chars"] for f in data["files"] if f["source"] == name)
        print(f"  {name}: {count} 篇 / {chars:,} 字符")
    print("主题：")
    counts = Counter(theme for f in data["files"] for theme in f["themes"])
    for name, count in counts.most_common():
        print(f"  {name}: {count}")
    print("子来源前 20：")
    for name, count in Counter(f["source_key"] for f in data["files"]).most_common(20):
        print(f"  {name}: {count}")


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else "report"
    data = build_manifest()
    if command == "write":
        if MANIFEST.exists() and "--force" not in sys.argv[2:]:
            existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
            validate_frozen_manifest(existing)
            # 白名单冻结后，译完的目标文件会自然离开 collect() 返回的“待译集合”。
            # 因此不能再拿动态待译集合与冻结清单做相等比较，否则每完成一篇反而
            # 会让清单自检失败。validate_frozen_manifest() 仍逐篇核验英文原文、
            # 中英映射、主题与当前筛选规则；只有显式 --force 才允许重建范围。
            print("B 类白名单已冻结且结构、路径和筛选规则一致")
            report(existing)
        else:
            MANIFEST.write_text(render(data), encoding="utf-8")
            print(f"已写入 {MANIFEST.relative_to(ROOT)}")
            report(data)
    elif command == "check":
        if not MANIFEST.exists():
            raise SystemExit(f"缺少 {MANIFEST.relative_to(ROOT)}")
        frozen = json.loads(MANIFEST.read_text(encoding="utf-8"))
        validate_frozen_manifest(frozen)
        print("冻结的 B 类白名单结构、路径和筛选规则一致")
        report(frozen)
    elif command == "report":
        if MANIFEST.exists():
            frozen = json.loads(MANIFEST.read_text(encoding="utf-8"))
            validate_frozen_manifest(frozen)
            report(frozen)
        else:
            report(data)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()

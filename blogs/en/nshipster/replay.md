---
title: Replay
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/replay/'
original_language: en
published: 2025-12-31
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:98455754000e7393'
translated: false
---

> 原文：[Replay](https://nshipster.com/replay/)　·　NSHipster (Mattt)

# [Replay](https://nshipster.com/replay/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 31^st, 2025

The year is 2025. You’re writing tests for networking code in your Swift app.

You could hit the live API, but then your tests are slow, flaky, and fail whenever that third-party service has a bad day. You could stub `URLSession`, but then you’re maintaining two implementations of your networking layer. You could maintain JSON fixtures by hand, but there’s no way to capture real responses automatically, so your fixtures go stale without anyone noticing.

There’s a better approach: **Record real HTTP traffic once, then replay it instantly for every subsequent test run.** This pattern has been battle-tested for over fifteen years in other languages.

[Replay](https://github.com/mattt/Replay) brings it to Swift.

---

In February 2010, [Myron Marston](https://github.com/myronmarston) created [VCR](https://github.com/vcr/vcr) for Ruby. Just like a videocassette recorder could capture television for later playback, VCR captured HTTP interactions so tests could replay them without hitting the network. Record once, play back forever.

The idea spread. Python got [VCR.py](https://github.com/kevin1024/vcrpy) and [pytest-recording](https://github.com/kiwicom/pytest-recording). Java got [Betamax](https://github.com/betamaxteam/betamax) (continuing the home video theme). Go got [go-vcr](https://github.com/dnaeon/go-vcr).

I’ve used VCR and pytest-recording for years and always missed having something comparable in Swift. [DVR](https://github.com/venmo/DVR) from Venmo came closest, using the same `URLProtocol` injection point that Replay uses. But it was built for a different era of Swift — before we had the tools to make something that felt really nice.

### For Auld Lang Syne

Being in conversation with that prior art means asking what’s different now. Two things stand out:

First, [HAR](https://en.wikipedia.org/wiki/HAR_%28file_format%29) became a _de facto_ standard. When Myron built VCR, there was no widely-adopted format for HTTP archives, so he invented one using YAML. That’s where the “cassette” terminology comes from. But around the same time, Jan Odvarko on the Firefox developer tools team was creating HAR (HTTP Archive). Today, every major browser exports HAR. As do Charles Proxy, Proxyman, mitmproxy, and Postman.

Replay uses HAR instead of inventing a new format. This means you can capture traffic from Safari’s Network tab and drop it directly into your test fixtures. You can inspect fixtures with any text editor.

Second, Swift finally has the extension points we need. Swift Testing traits — especially the [`TestScoping` protocol](https://developer.apple.com/documentation/testing/testscoping) from Swift 6.1 — enable the kind of declarative, per-test configuration that pytest fixtures provide. Package plugins let us build integrated tooling that feels native.

These capabilities simply didn’t exist before — not in any way that felt intuitive or convenient.

---

## How Replay Works

Add `.replay` to a test and Replay intercepts HTTP requests, serving responses from a HAR file instead of hitting the network:

```
import Testing
import Replay

struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

@Test(.replay("fetchUser"))
func fetchUser() async throws {
    let (data, _) = try await URLSession.shared.data(
        from: URL(string: "https://api.example.com/users/42")!
    )
    let user = try JSONDecoder().decode(User.self, from: data)
    #expect(user.id == 42)
}
```

The `.replay("fetchUser")` trait loads responses from `Replays/fetchUser.har`. Your production code uses `URLSession` normally. No protocols to define. No mocks to inject. Replay’s interception uses built-in affordances in the [Foundation URL Loading System](https://developer.apple.com/documentation/foundation/url-loading-system), so it works with `URLSession.shared`, custom sessions, and libraries like [Alamofire](https://nshipster.com/alamofire).

### The Recording Workflow

The first time you run a test with `.replay`, it fails intentionally:

```
❌  Test fetchUser() recorded an issue at ExampleTests.swift
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  No Matching Entry in Archive
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Request: GET https://api.example.com/users/42
Archive: /path/to/.../Replays/fetchUser.har

This request was not found in the replay archive.

Options:
1. Run against the live network:
   REPLAY_PLAYBACK_MODE=live swift test --filter <test-name>

2. Record the archive:
   REPLAY_RECORD_MODE=once swift test --filter <test-name>
```

This is deliberate. Accidental recording could capture credentials, PII, or session tokens. By requiring you to opt into recording explicitly, Replay ensures you’re always aware when network traffic is being captured.

So let’s do that now:

```
REPLAY_RECORD_MODE=once swift test --filter fetchUser
```

This hits the real API, captures the response, and saves it to `Replays/fetchUser.har`. From then on, the test runs instantly against the recorded fixture. There’s something deeply satisfying about watching a test suite that used to take minutes finish in seconds.

### What’s in a HAR File

A HAR file is just JSON:

```
{
  "log": {
    "version": "1.2",
    "creator": { "name": "Replay", "version": "1.0" },
    "entries": [
      {
        "request": {
          "method": "GET",
          "url": "https://api.example.com/users/42",
          "headers": [{ "name": "Accept", "value": "application/json" }]
        },
        "response": {
          "status": 200,
          "content": {
            "mimeType": "application/json",
            "text": "{\"id\":42,\"name\":\"Alice\"}"
          }
        }
      }
    ]
  }
}
```

Human-readable. Editable. Compatible with a vast ecosystem of tools. 🧑‍🍳💋

## Handling Sensitive Data

HAR files have a way of accumulating secrets. Session cookies, authorization headers, API keys — all captured faithfully alongside the responses you actually care about.

Replay addresses this with filters that strip sensitive data during recording:

```
@Test(
    .replay(
        "fetchUser",
        filters: [
            .headers(removing: ["Authorization", "Cookie"]),
            .queryParameters(removing: ["token", "api_key"])
        ]
    )
)
func fetchUser() async throws { /* ... */ }
```

The general principle: configure filters before recording, not after.

## Flexible Matching

By default, Replay matches requests by HTTP method and full URL. For APIs with volatile query parameters (pagination cursors, timestamps, cache-busters), you can configure looser matching:

```
@Test(.replay("fetchUser", matching: [.method, .path]))
func fetchUser() async throws { /* ... */ }
```

Available matchers include `.method`, `.url`, `.host`, `.path`, `.query`, `.headers([...])`, `.body`, and `.custom(...)` for arbitrary logic.

## Inline Stubs

Replay also supports inline stubs:

```
@Test(
    .replay(
        stubs: [
            .get("https://api.example.com/health", 200, ["Content-Type": "application/json"], {
                #"{"status": "ok"}"#
            })
        ]
    )
)
func testHealthCheck() async throws {
    let (data, _) = try await URLSession.shared.data(
        from: URL(string: "https://api.example.com/health")!
    )
    #expect(String(data: data, encoding: .utf8) == #"{"status": "ok"}"#)
}
```

This is useful for testing error handling, edge cases, or scenarios where the response content matters less than the status code.

---

Fifteen years of refinement across Ruby, Python, JavaScript, and other ecosystems have established clear best practices for HTTP recording: capture real traffic, strip sensitive data, fail fast when fixtures are missing, provide good error messages when things go wrong. Replay brings all of that to Swift.

If you’ve been struggling with flaky API tests, or putting off testing your network code because the overhead felt too high, resolve to give Replay a try.

[Replay is open source on GitHub.](https://github.com/mattt/Replay) Let me know what you think!

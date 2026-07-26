---
title: op run
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/1password-cli/'
original_language: en
published: 2025-01-01
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:5617d9013b23a74b'
translated: false
---

> 原文：[op run](https://nshipster.com/1password-cli/)　·　NSHipster (Mattt)

# [op run](https://nshipster.com/1password-cli/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  January 1^st, 2025

`.env` files. If you’ve worked on a web application, you’ve probably seen one.

While they certainly get the job done, `.env` files have shortcomings that can create friction in development workflows.

We’ve touched on `.env` files in past articles about [xcconfig](https://nshipster.com/xcconfig/) files and [secret management on iOS](https://nshipster.com/secrets/). But this week on NSHipster we’re taking a deeper look, exploring how the lesser-known [1Password CLI](https://developer.1password.com/docs/cli/get-started/) (`op`) can solve some problems many of us face managing secrets day-to-day.

---

## The Problem of Configuration

Around 2011, Adam Wiggins published [“The Twelve-Factor App”](https://12factor.net), a methodology for building modern web applications that has since become canon in our industry.

The third of those twelve factors, [“Config”](https://12factor.net/config), prescribes storing configuration in environment variables:

> “Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires **strict separation of config from code**. Config varies substantially across deploys, code does not.”

This core insight — that configuration should be separate from code — led to the widespread adoption of `.env` files.

A typical `.env` file looks something like this:

```
DATABASE_URL=postgres://localhost:5432/myapp_development
REDIS_URL=redis://localhost:6379/0
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=wJa...
STRIPE_SECRET_KEY=sk_test_...
```

You add this file to `.gitignore` to keep it out of version control, and load these variables into your environment at runtime with a tool or library.

Simple enough. So what’s the problem?

### .env Files in Practice

Despite their apparent simplicity, `.env` files introduce several points of friction in development workflows:

First, there’s the perennial issue of onboarding: How does a new team member get what they need to run the app locally? The common solution is to have a `.env.sample` / `.env.example` file in version control, but this creates a maintenance burden to keep it in sync with the actual requirements. And in any case, developers still need to go on a scavenger hunt to fill it out before they can be productive.

Then there’s the multi-environment problem: As soon as you need different configurations for development, staging, and production, you end up with a proliferation of files: `.env.development`, `.env.test`, `.env.staging`… Each requiring its own `.sample` / `.example` counterpart.

But perhaps most pernicious is the challenge of managing changes to configuration over time. Because `.env` files aren’t in version control, changes aren’t, you know… _tracked anywhere_ 🥲

## Enter the 1Password CLI (`op`)

You may already use [1Password](https://1password.com) to manage your passwords and other secrets. But what you might not know is that 1Password also has a CLI that can integrate directly with your development workflow.

`op` lets you manage 1Password from the command-line. You can do all the CRUD operations you’d expect for items in your vault. But its killer features is the `op run` subcommand, which can dynamically inject secrets from your 1Password vault into your application’s environment.

Instead of storing sensitive values directly in your `.env` file, you reference them using special `op://` URLs:

```
# .env
IRC_USERNAME=op://development/chatroom/username
IRC_PASSWORD=op://development/chatroom/password
```

```
import Foundation

guard let username = ProcessInfo.processInfo.environment["IRC_USERNAME"],
     let password = ProcessInfo.processInfo.environment["IRC_PASSWORD"] else {
   fatalError("Missing required environment variables")
}

// For testing only - never print credentials in production code
print(password)
```

Run this on its own, and you’ll fail in proper 12 Factor fashion:

```
$ swift run
❗️ "Missing required environment variables"
```

But by prepending `op run` we read in that `.env` file, resolve each vault item reference, and injects those values into the evironment:

```
$ op run -- swift run
hunter2
```

You’re even prompted to authorize with Touch ID the first time you invoke `op run`.

![1Password Create Vault dialog](https://nshipster.com/assets/1password-authorize--light-a603cb0d66d88414549464ef558e4d72b30cb6b6ce0bd0507a9b2d4a936dfb11a8822079dea904d843875e48f8d9dc2a906d9d82b8177e9e2fe9a9320e2b4e03.png)

---

Ready to give this a test drive? Here’s how to get started:

## A Step-By-Step Guide to Using the 1Password CLI in .env Files

### Step 1: Install and Configure the 1Password CLI

On macOS, you can install the CLI with [homebrew](https://brew.sh/):

```
$ brew install 1password-cli
```

Then, in the 1Password app, open Settings (⌘,), go to the Developer section, and check the box labeled “Integrate with 1Password CLI”.

![1Password Settings](https://nshipster.com/assets/1password-settings--light-d793948bc993ebd4d35317ef922a401cf9a06e6155ab312ac4c0e9fb3e45e52cb83eca546c8ce6b3ae3249d8052b23ddd8f8c39d57d626b897ac50d7fed0fb23.png)

Running any `op` subcommand should prompt you to connect to the app.

If you get off the happy path, consult [the official docs](https://developer.1password.com/docs/cli/get-started/) to get back on track.

### Step 2: Create a Shared Vault

Create a new vault in 1Password specifically for development secrets. Give it a clear name like “Development” and a useful description.

![1Password Create Vault dialog](https://nshipster.com/assets/1password-create-vault--light-14040f422f6b39b6b84e9266dea5859f944f65344948dd8b373cc3734de98ace845fc1c7590aaf270c0295ff296420ce9bccb6aafa7b3d0ae879b58e6f673a33.png)

### Step 3: Migrate Existing Secrets

For each entry in your `.env` file, create a corresponding item in 1Password. Choose the appropriate item type:

![](https://nshipster.com/assets/1password-api-credential-f848f27796dc0008b214bed990e11a0c521e0ae427b8cf3e9b54ce97895c5275b9c02b4ef9d6aae4800de2d0695c85c6d640e627332ee29b15951c886ea96520.png)

**API Credential**

For third-party service API keys

Fields: username, credential

![](https://nshipster.com/assets/1password-password-61b2ba71f1864985527199951225465adacab9415813e76ff6de67a0522f7da58c8bf6724e1fc0a1e426a419e8eaba81acbe9ee3ca16bd36f84957e58d5fd61f.png)

**Password**

For first-party secrets, like encryption keys

Fields: username, password

![](https://nshipster.com/assets/1password-database-9109b5422bd1ce3792c53fb8c44d1b7893738b10dbcd0fe39e471dae36ca5f6385832d2e6982c614c013741a0ab9da4c7c44b464c1756a08cd88c11880478b41.png)

**Database**

For hosted PostgreSQL databases and the like

Fields: type, server, port, database, username, password

### Step 4: Update Your .env File

Replace raw values in your `.env` file with `op://` references using the following format:

```
op://vault/item/field
```

Each reference consists of three components:

- The vault name (e.g., “development”)
- The item name or UUID
- The field name from the item

For example, here’s how you might reference credentials for various services:

```
# Reference by item name (case-insensitive)
AWS_ACCESS_KEY_ID=op://development/AWS/username
AWS_SECRET_ACCESS_KEY=op://development/WorkOS/credential

# Reference by item UUID
STRIPE_SECRET_KEY=op://development/abc123xyz789defghijklmnop/password

# Using different field names based on item type
DATABASE_HOST=op://development/db/server
DATABASE_USER=op://development/db/username
DATABASE_PASSWORD=op://development/db/password
DATABASE_NAME=op://development/db/database
```

You can locate the UUID for any item in 1Password by clicking the "More actions" button (⋮, _whatever you want to call that_) and selecting "Copy item UUID".

Both item name and UUID references work, but using UUIDs can be more reliable in automation contexts since they're guaranteed to be unique and won't change if you rename the item.

![1Password Copy Item UUID](https://nshipster.com/assets/1password-copy-uuid--light-a6301b3bfce557550474188650f4c4860327b1f84560d414bb6f284262c82fc97f3db2418a61c249cb7b4e764b45881a96266bc943d1fc1633c05da8a43b81f2.png)

Once you’ve replaced all sensitive values with `op://` references, you can safely commit your `.env` file to version control. The references themselves don’t contain any sensitive information – they’re just pointers to your 1Password vault.

### Step 5. Update Your Development Script

Whatever command you normally run to kick off your development server, you’ll need to prepend `op run --` to that.

For example, if you follow the [“Scripts to Rule Them All”](https://github.com/github/scripts-to-rule-them-all) pattern, you’d update `script/start` like so:

```
#!/bin/sh

- swift run
+ op run -- swift run
```

### Advantages Over Traditional .env Files

`op run` solves many of the problems inherent to `.env` files:

- **No More Cold Start Woes**: New team members get access to all required configuration simply by joining the appropriate 1Password vault.
- **Automatic Updates**: When credentials change, they’re automatically updated for everyone on the team. No more out-of-sync configuration.
- **Proper Secret Management**: 1Password provides features like access controls, versioning, and integration with [Have I Been Pwned](https://haveibeenpwned.com/).

## Potential Gotchas

Like any technical solution, there are some trade-offs to consider:

- **Performance**: `op run` adds a small overhead to command startup time (typically less than a second). ^[1](https://1password.community/discussion/145854/op-read-is-pretty-slow-700ms-per-invocation)
- **stdout/stderr Handling**: As mentioned above, `op run` modifies `stdout`/`stderr` to implement secret masking, which can interfere with some terminal applications. ^[2](https://1password.community/discussion/145938/op-run-changes-stdout-and-stderr-to-not-be-ttys-when-masking)
- **Dev Container Support**: If you use [VSCode Dev Containers](https://containers.dev/overview), you may encounter some friction with the 1Password CLI. ^[3](https://1password.community/discussion/147554/feature-request-first-class-support-for-dev-containers-and-op-cli)

## Driving Technical Change

The implementation is often the easy part. The real challenge can be getting your team on board with the change.

First, state the problem you’re trying to solve. Change for change’s sake is rarely helpful.

Next, figure out who you need to get buy-in from. Talk to them. Articulate specific pain point that everyone recognizes, like the frustration of onboarding new team members or the time wasted debugging configuration-related issues.

Once you’ve gotten the green light, move slowly but deliberately. Start small by migrating a single credential, or maybe all of the credentials in a smaller project. Build up confidence that this approach is a good fit — both technically and socially.

---

Managing development secrets is one of those problems that seems trivial at first but can become a significant source of friction as your team and application grow.

The 1Password CLI offers a more sophisticated approach that integrates with tools developers already use and trust.

While it may not be the right solution for every team, it’s worth considering if you’re feeling the pain of traditional `.env` files.

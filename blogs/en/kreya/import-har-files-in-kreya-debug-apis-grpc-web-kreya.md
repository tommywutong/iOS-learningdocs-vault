---
title: 'Import HAR Files in Kreya: Debug APIs & gRPC-Web | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/har-import/'
original_language: en
published: 2025-05-14
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ade0ddbc30372bba'
translated: false
---

> 原文：[Import HAR Files in Kreya: Debug APIs & gRPC-Web | Kreya](https://kreya.app/blog/har-import/)　·　Kreya Blog

Kreya has introduced a powerful new feature: **HAR file import!** This update makes analysing, replaying and debugging HTTP and gRPC-Web requests directly in Kreya easier than ever. In this post, we’ll show you how to export HAR files from browsers and import them into Kreya. We will also explain why this is a secure and essential workflow for developers, particularly those working with gRPC-Web APIs.

## What is a HAR file?

A HAR (HTTP Archive) file is a standardised format for capturing all the network requests and responses made by your browser. Including headers, payloads, cookies and more, it is invaluable for debugging APIs and web applications.

## How to export a HAR File from browsers

note

HAR files may contain sensitive information, such as authentication tokens, cookies and request/response bodies. Always handle them securely. Kreya helps with this by storing all imported HAR data locally on your machine, so no data ever leaves your device unintentionally and you can safely analyse even sensitive HAR files.

### Exporting a HAR file in Chrome

1. Open Chrome DevTools (right-click → Inspect, or press F12).
2. Go to the **Network** tab.
3. _(optional)_ Enable **Preserve log** and **Disable cache** to capture all requests, including those during page reloads or redirects.
4. _(optional)_ To ensure all sensitive data (including request/response bodies) is included, you can execute the following command in the DevTools Console before exporting:  
  4.1. Open the command palette in the DevTools by pressing Ctrl+⇧+P.  
  4.2. Run the command `Allow to generate HAR with sensitive data`.
5. Reproduce the workflow you want to capture.
6. Click the downward pointing arrow and save the HAR file to your computer.

    - Alternatively, you can right-click on any network request and select **Copy → Copy all as HAR**.

### Exporting a HAR file in Firefox

1. Open Firefox Developer Tools (Right-click → Inspect, or press F12).
2. Go to the **Network** tab.
3. Enable **Disable cache** to capture all requests.
4. Reproduce the workflow you want to capture.
5. Right-click anywhere in the list of network requests and select **Save All As HAR** and save the file to your computer.

### Exporting a HAR file in Safari

1. Enable the Develop menu (Safari → Settings → Advanced → Show features for web developers).
2. Open the **Web Inspector** (Develop → Show Web Inspector or F12).
3. Go to the **Network** tab.
4. Enable **Disable cache** to capture all requests.
5. Perform the actions you want to capture.
6. Click **Export** and save the har file to your computer.

## How to import a HAR file in Kreya

If you have copied the HAR contents to your clipboard, simply open Kreya, and it will automatically detect the HAR content and prompt you to import it. Just click **Import**. If you saved to a HAR file, follow these steps to import it:

1. Open Kreya.
2. Open the command palette with Ctrl+K.
3. Select the import action.
4. Select the `HAR` import type.
5. Choose your `.har` file.
6. Click **Import**.
7. Kreya will automatically parse the file and create requests for each entry, including all headers, payloads, and metadata.
8. You can now replay, modify, or analyze these requests directly in Kreya.

## gRPC-Web: decode and debug with ease

HAR files can also capture **gRPC-Web** requests, which are commonly used in modern web applications. Kreya’s HAR import feature is especially useful here:

- If you import your proto definitions into Kreya via an [importer](https://kreya.app/docs/importers/grpc/), it will **decode gRPC-Web payloads** automatically.
- This means you can inspect, replay, and debug gRPC-Web requests just like regular HTTP requests.
- No more struggling with base64 or binary payloads. Kreya makes them human-readable.

![An animation showcasing importing requests with a HAR file.](https://kreya.app/whats-new/1.17/har_import.gif)

## Privacy & security: your data stays local

Kreya is designed with privacy in mind. All imported HAR data is stored **locally** on your machine. No data is sent to external servers or leaves your device unintentionally. This is especially important when working with HAR files that may contain sensitive information. Kreya ensures that your data remains secure and private.

## Why use Kreya for HAR file analysis?

- **Comprehensive HAR import**: Bring all your HTTP and gRPC-Web requests into one place.
- **Local-first privacy**: Sensitive data never leaves your machine.
- **Advanced gRPC-Web support**: Decode and analyze gRPC-Web payloads with imported protos.
- **Replay and modify requests**: Easily debug and test APIs using real captured traffic.

## Conclusion

Kreya's HAR import feature streamlines your API debugging workflow. It keeps your data secure and offers unmatched support for gRPC-Web. Experience a new level of productivity and security in API development — try it out today!

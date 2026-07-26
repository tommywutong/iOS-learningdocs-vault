---
title: 'Kreya 1.17 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.17-whats-new/'
original_language: en
published: 2025-04-30
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13cb5d767f877d05'
translated: false
---

> 原文：[Kreya 1.17 - What's New | Kreya](https://kreya.app/blog/kreya-1.17-whats-new/)　·　Kreya Blog

Kreya 1.17 comes with the new Kreya Script, which can control operation invocation with JavaScript. Support has been added for importing HAR files, the JWT auth provider, exporting operations as cURL and gRPCurl commands and many more features have been implemented.

### New Kreya Script [Pro / Enterprise](https://kreya.app/pricing/)

This release introduces a new way of scripting in Kreya. It's now possible to create a script outside the context of an operation. To do this, you can create a script file and call an operation with plain JavaScript.

![An animation showcasing creating an Kreya Script and running it.](https://kreya.app/whats-new/1.17/script.gif)

Calling operations multiple times, waiting for a response and so on, you are completely free to do anything in this script. Here is an example of what a script might look like.

```javascript
// Invoke an operation that starts a long running job on the serverawait kreya.invokeOperation('start-long-running-job');let finished = false;while (!finished) {  const result = await kreya.invokeOperation('fetch-job-status');  finished = result.success;  if (!finished) {    kreya.sleep(500);  }}// Now invoke an operation that fetches the job result and performs tests on itawait kreya.invokeOperation('fetch-job-result');
```

See the [documentation](https://kreya.app/docs/scripting-and-tests/invoker-scripts/) for more examples and information. This feature can only be used with a Pro or Enterprise plan, if you want to give this a try, there is a [10 day trial period](https://kreya.app/pricing/).

### Importing HAR files

A disadvantage of gRPC over REST is browser support. You cannot just look at a request in the browser's development tools. You have to decode everything first. This is sort of fixed with the new HAR file import. You can simply export your requests to a HAR file in the browser's development tools and import it into Kreya. If the proto files for those requests are present in Kreya, you can simply read each request and response in Kreya.

![An animation showcasing importing requests with a HAR file.](https://kreya.app/whats-new/1.17/har_import.gif)

### JWT (signed with a static key) auth provider

A new auth provider is available with the new release: JWT (signed with a static key). To create such an auth config, just open the authentications tab and create one with this type and fill in all the details.

![An animation showcasing creating an JWT auth config.](https://kreya.app/whats-new/1.17/jwt.gif)

### Exporting operations as cURL and gRPCurl commands

Operations can be exported as cURL and gRPCurl commands. Simply open the context menu of an operation and copy it to the clipboard.

![An animation showcasing exporting operations as cURL command.](https://kreya.app/whats-new/1.17/curl.gif)

### User variables editor

User variables can now be viewed and edited in `Project > User variables`. You can set a user variable in scripts with `kreya.variables.set("hello", "world");`.

![An animation showcasing viewing user variables.](https://kreya.app/whats-new/1.17/user_variables.gif)

### Searching for operations, directories and collections

We have also implemented a quick search in the operation list to find operations, directories and collections. Just click on the new search button or press Ctrl+F or ⌘+F and enter your search string.

![An animation showcasing searching operations, directories and collections.](https://kreya.app/whats-new/1.17/search.gif)

### Support reading and writing files in scripting API [Pro / Enterprise](https://kreya.app/pricing/)

It is now possible to read and write files from your operation script. This can be used for snapshot testing, for example.

```javascript
import { expect } from 'chai';import { readFile } from 'fs/promises';const verified = await readFile('say_hello.verified.txt', 'utf8');kreya.grpc.onResponse(msg => {  kreya.test('Verify response', () => expect(msg.content.message).to.eql(verified));});
```

See the [documentation](https://kreya.app/docs/scripting-and-tests/general/fs-script-api/) for more examples and information.

### Connecting via unix-socket (e.g. to the Docker daemon)

You can now connect via unix-socket with a normal REST request. Just enter a valid unix-socket address in the endpoint field (e.g. for the Docker daemon `unix:///var/run/docker.sock`) and send your request.

![An animation showcasing connecting via unix-socket.](https://kreya.app/whats-new/1.17/unix_socket.gif)

See the [documentation](https://kreya.app/docs/unix-sockets/) for more examples and information.

### Use native browser in auth configs

Using the native browser opens the default browser of your system instead of Kreya's built-in web window. This approach allows you to leverage browser extensions, password managers, passkeys, and other browser-specific features. However, it requires a localhost redirect URI with an available port to complete the authentication flow.

![An animation showcasing using native browser in auth configs.](https://kreya.app/whats-new/1.17/native_browser.gif)

### Bug fixes

Many bugs have been fixed. More details can be found on our [release notes](https://kreya.app/docs/release-notes/) page.

If you find a bug, please do not hesitate to [report](https://github.com/riok/Kreya/issues/new/choose) it. You can contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#3e565b5252517e554c5b475f105f4e4e) for any further information or feedback.

Stay tuned! 🏄

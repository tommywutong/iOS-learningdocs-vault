---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/Bots.html
archived_at: '2026-07-18T02:24:22.599530Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Bots

Bots are processes that Xcode Server runs to perform integrations on the current version of a project in a source code repository. An integration is a single run of a bot. Integrations consist of building, analyzing, testing, and archiving the apps (or other software products) defined in your Xcode projects. With Xcode Server able to access the source code repositories of those projects, you can configure bots to perform continuous integrations on them. Bots can be configured to run in the following ways:

- Every time a change is committed to the repository
- On a regular schedule, such as hourly, daily, or weekly
- When manually initiated

### Creating a New Bot

__POST__

`/bots`

Creates a new bot.

__Example__

`https://server.mycompany.com:20343/api/bots`

__Request__

_Body_

1. `{`
2. `"configuration": {`
3. `...`
4. `},`
5. `"name": "Sketch"`
6. `}`

__Response__: `201`

_Headers_

1. `Content-Type: application/json`
2. `Location: https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b`
3. `X-XCSAPIVersion: 4`

_Body_

1. `{`
2. `"_id": "6f0faeb1cc4c55e174cac5ff8100f13b",`
3. `"_rev": "11-1339f79e58100e9befc1451fe906e142",`
4. `"configuration": {`
5. `...`
6. `},`
7. `"name": "Sketch",`
8. `"doc_type": "bot"`
9. `}`

__Response__: `400`

_Body_

1. `{`
2. `status: 400,`
3. `message: "The body is empty"`
4. `}`

### Retrieving Bots

__GET__

`/bots`

Retrieves a list of bots.

__Example__

`https://server.mycompany.com:20343/api/bots`

__Response__: `200`

_Body_

1. `{`
2. `"counter": 1,`
3. `"results": [`
4. `{`
5. `"_id": "6f0faeb1cc4c55e174cac5ff8100f13b",`
6. `"_rev": "11-1339f79e58100e9befc1451fe906e142",`
7. `"configuration": {`
8. `...`
9. `},`
10. `"name": "Sketch",`
11. `"doc_type": "bot"`
12. `}`
13. `]`
14. `}`

### Retrieving a Bot

__POST__

`/bots/{id}`

Retrieves a single bot.

__Example__

`https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

__Response__: `200`

_Body_

1. `{`
2. `"_id": "6f0faeb1cc4c55e174cac5ff8100f13b",`
3. `"_rev": "11-1339f79e58100e9befc1451fe906e142",`
4. `"configuration": {`
5. `...`
6. `},`
7. `"name": "Sketch",`
8. `"doc_type": "bot"`
9. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Bot not found"`
4. `}`

### Updating a Bot

__PATCH__

`/bots/{id}`

Updates a single bot. This method will merge the provided blueprint with the existing authenticated source control blueprint.

__Example__

`https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

__Request__

_Body_

1. `{`
2. `"name": "Sketch Demo"`
3. `}`

__Response__: `200`

_Body_

1. `{`
2. `"_id": "6f0faeb1cc4c55e174cac5ff8100f13b",`
3. `"_rev": "11-1339f79e58100e9befc1451fe906e142",`
4. `"configuration": {`
5. `...`
6. `},`
7. `"name": "Sketch",`
8. `"doc_type": "bot"`
9. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Bot not found"`
4. `}`

### Deleting a Bot

__DELETE__

`/bots/{id}`

Deletes a single bot.

__Example__

`https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

__Request__

_Body_

1. `{`
2. `"name": "Sketch Demo"`
3. `}`

__Response__: `204`

__Response__: `204`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Bot not found"`
4. `}`

### Duplicating a Bot

__POST__

`/bots/{id}/duplicate`

Duplicates an existing bot. Optionally, the body of the request may specify the properties to be set after the bot has been duplicated. If the body is empty, the duplicated bot will be an exact copy of the original.

__Example__

`https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b/duplicate`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

__Request__

_Body_

1. `{`
2. `"name": "My new bot"`
3. `}`

__Response__: `201`

_Headers_

1. `Content-Type: application/json`
2. `Location: https://server.mycompany.com:20343/api/bots/e2d2444f20d5a86015fdc69adb000c67`
3. `X-XCSAPIVersion: 4`

_Body_

1. `{`
2. `"_id": "add0cd57-42a4-4684-9a11-7fb01cb86d5a",`
3. `"_rev": "11-497507e3-9078-4664-be8b-022ec0f13ee7",`
4. `"configuration": {`
5. `...`
6. `},`
7. `"name": "My new bot",`
8. `"doc_type": "bot"`
9. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Bot not found"`
4. `}`

[Overview](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmjnknltc)

[Integrations](Integrations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmznknlte)

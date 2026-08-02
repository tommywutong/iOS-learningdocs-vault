---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/Integrations.html
archived_at: '2026-07-18T02:24:24.062465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Integrations

An integration is a single execution of your bot.

### Creating a New Integration

__POST__

`API`

Begins an integration for the specified bot.

Optionally, you can specify `shouldClean` in the request body to indicate whether the integration should be performed using the latest sources.

__Example__

`https://server.mycompany.com:20343/api/bots/6f0faeb1cc4c55e174cac5ff8100f13b/integrations`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

__Request__

_Body_

1. `{`
2. `shouldClean: false`
3. `}`

__Response__: `201`

_Headers_

1. `Content-Type: application/json`
2. `Location: https://server.mycompany.com:20343/integration/b31ad8317300e89b2db73aad3d0194ad`
3. `X-XCSAPIVersion: 4`

_Body_

1. `{`
2. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
3. `"_rev": "3-51e9bed938b457df5bce57bca7625af2",`
4. `"bot": {`
5. `...`
6. `},`
7. `"shouldClean": false,`
8. `"currentStep": "pending",`
9. `"number": 1,`
10. `"queuedDate": "2015-07-20T20:27:22.516Z",`
11. `"success_streak": 0,`
12. `"doc_type": "integration"`
13. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Retrieving an Integration

__GET__

`/integrations/{id}`

Retrieves a single integration.

__Example__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `200`

_Body_

1. `{`
2. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
3. `"_rev": "17-869fccee9b37638a719c20b1dcfa6869",`
4. `"number": 1,`
5. `"result": "succeeded",`
6. `"success_streak": 1,`
7. `"bot": {`
8. `...`
9. `},`
10. `"shouldClean": false,`
11. `"doc_type": "integration",`
12. `"currentStep": "completed",`
13. `"queuedDate": "2015-07-20T21:30:58.971Z",`
14. `"buildServiceFingerprint": "9C:67:D4:4A:00:97:0F:22:7B:B1:68:7E:28:1D:E0:5E:F2:E4:45:7C",`
15. `"startedTime": "2015-07-20T21:30:59.669Z",`
16. `"revisionBlueprint": {`
17. `...`
18. `},`
19. `"buildResultSummary": {`
20. `"analyzerWarningCount": 0,`
21. `"testFailureCount": 0,`
22. `"testsChange": 220,`
23. `"errorCount": 0,`
24. `"testsCount": 220,`
25. `"testFailureChange": 0,`
26. `"warningChange": 0,`
27. `"regressedPerfTestCount": 0,`
28. `"warningCount": 0,`
29. `"errorChange": 0,`
30. `"improvedPerfTestCount": 0,`
31. `"analyzerWarningChange": 0,`
32. `"codeCoveragePercentage": 0,`
33. `"codeCoveragePercentageDelta": 0`
34. `},`
35. `"endedTime": "2015-07-20T21:31:23.906Z",`
36. `"endedTimeDate": [`
37. `2015,`
38. `7,`
39. `20,`
40. `21,`
41. `31,`
42. `23,`
43. `906`
44. `],`
45. `"duration": 24.237,`
46. `"ccPercentage": 0,`
47. `"ccPercentageDelta": 0,`
48. `"testedDevices": [`
49. `{`
50. `"osVersion": "10.11",`
51. `"connected": true,`
52. `"simulator": false,`
53. `"modelCode": "MacBookPro11,3",`
54. `"deviceType": "com.apple.mac",`
55. `"modelName": "MacBook Pro",`
56. `"revision": "3-824d6d3e1adedab99b103ab21f6b330d",`
57. `"modelUTI": "com.apple.macbookpro-15-retina-display",`
58. `"name": "server.mycompany.com",`
59. `"trusted": true,`
60. `"doc_type": "device",`
61. `"supported": true,`
62. `"processor": "2.5 GHz Intel Core i7",`
63. `"identifier": "686EE427-E12F-50DF-9D20-455B7E3F15CE-x86_64",`
64. `"enabledForDevelopment": true,`
65. `"serialNumber": "XYZ",`
66. `"platformIdentifier": "com.apple.platform.macosx",`
67. `"ID": "b31ad8317300e89b2db73aad3d005719",`
68. `"architecture": "x86_64",`
69. `"retina": false,`
70. `"isServer": true`
71. `}`
72. `],`
73. `"testHierarchy": {`
74. `"Sketch": {`
75. `"SketchTests": {`
76. `"testFileWithPath": {`
77. `"676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64": 1`
78. `},`
79. `"testInitiWithPath": {`
80. `"676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64": 1`
81. `}`
82. `}`
83. `}`
84. `},`
85. `"perfMetricNames": [`
86. `"Time"`
87. `],`
88. `"perfMetricKeyPaths": [`
89. `"Sketch.SketchTests.testPerfOpenFile"`
90. `]`
91. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Deleting an Integration

__DELETE__

`/integrations/{id}`

Deletes an integration.

__Example__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `204`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Canceling an Integration

__POST__

`API`

Cancels a integration currently being executed.

__Example__

`/integrations/{id}/cancel`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `204`

__Response__: `400`

_Body_

1. `{`
2. `"status": 400,`
3. `"message": "The integration cannot be canceled because it has been completed already"`
4. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Filtering Integrations for a Bot

__GET__

`/bots/{id}/integrations{?filter,last,number,from,next,prev,count,summary_only}`

Retrieve options to perform filters, selections and calculations on all integrations for the specified bot. There are two filter options: non_fatal and with_build_results.

- non_fatal: Integrations with a result of type succeeded, test-failures, build-errors, warnings, analyzer-warnings or build-failed.
- with_build_results: Integrations containing build summary information.

__Examples__

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?filter=non_fatal`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?filter=non_fatal&last=50`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?filter=with_build_results`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?filter=with_build_results&last=15`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?last=1`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?number=1`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?from=3&next=2`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?last=1&summary_only=true`

`https://server.mycompany.com:20343/api/bots/68a5sdf67/integrations?count=true`

__Parameters__

_id_ (required)

- The bot ID.
- Type: `string`
- Example: `6f0faeb1cc4c55e174cac5ff8100f13b`

_filter_ (optional)

- Choices: `non_fatal`, `with_build_results`
- Type: `string`

_last_ (optional)

- On output, the last specified number of integrations for the specified bot.
- Type: `number`

_number_ (optional)

- On output, the integration with the given number for the specified bot.
- Type: `number`

_from_ (optional)

- The integration number from which to start filtering. This option requires `next` or `prev` to be specified as well.
- Type: `number`

_next_ (optional)

- It indicates the number of integrations you want filtered beyond the starting point. This option requires `from` to be specified as well.
- Type: `number`

_prev_ (optional)

- It indicates the number of integrations you want filtered beyond the starting point. This option requires `from` to be specified as well.
- Type: `number`

_count_ (optional)

- On output, the number of integrations for the specified bot.
- Type: `number`

_summary_only_ (optional)

- A Boolean value that indicates whether to return a brief summary instead of the regular payload.
- Type: `boolean`

__Response__: `200`

_Body_

1. `{`
2. `"count": 1,`
3. `"results": [`
4. `{`
5. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
6. `"_rev": "17-869fccee9b37638a719c20b1dcfa6869",`
7. `"number": 1,`
8. `"result": "succeeded",`
9. `"success_streak": 1,`
10. `"bot": {`
11. `...`
12. `},`
13. `"shouldClean": false,`
14. `"doc_type": "integration",`
15. `"currentStep": "completed",`
16. `"queuedDate": "2015-07-20T21:30:58.971Z",`
17. `"buildServiceFingerprint": "9C:67:D4:4A:00:97:0F:22:7B:B1:68:7E:28:1D:E0:5E:F2:E4:45:7C",`
18. `"startedTime": "2015-07-20T21:30:59.669Z",`
19. `"revisionBlueprint": {`
20. `...`
21. `},`
22. `"buildResultSummary": {`
23. `"analyzerWarningCount": 0,`
24. `"testFailureCount": 0,`
25. `"testsChange": 220,`
26. `"errorCount": 0,`
27. `"testsCount": 220,`
28. `"testFailureChange": 0,`
29. `"warningChange": 0,`
30. `"regressedPerfTestCount": 0,`
31. `"warningCount": 0,`
32. `"errorChange": 0,`
33. `"improvedPerfTestCount": 0,`
34. `"analyzerWarningChange": 0,`
35. `"codeCoveragePercentage": 0,`
36. `"codeCoveragePercentageDelta": 0`
37. `},`
38. `"endedTime": "2015-07-20T21:31:23.906Z",`
39. `"endedTimeDate": [`
40. `2015,`
41. `7,`
42. `20,`
43. `21,`
44. `31,`
45. `23,`
46. `906`
47. `],`
48. `"duration": 24.237,`
49. `"ccPercentage": 0,`
50. `"ccPercentageDelta": 0`
51. `}`
52. `]`
53. `}`

__Response__: `400`

_Body_

1. `{`
2. `"status": 400,`
3. `"message": "Bad request: filter 'foobar' is not supported"`
4. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Filtering Integrations for All Bots

__GET__

`/integrations{?filter,last,count,summary_only}`

Retrieve options to perform filters, selections and calculations on all integrations. There are two filter options: non_fatal and with_build_results.

- `non_fatal`: Integrations with a result of type `succeeded`, `test-failures`, `build-errors`, `warnings`, `analyzer-warnings` or `build-failed`.
- `with_build_results`: Integrations containing build summary information.

__Example__

`https://server.mycompany.com:20343/api/integrations?filter=non_fatal`

`https://server.mycompany.com:20343/api/integrations?filter=non_fatal&last=50`

`https://server.mycompany.com:20343/api/integrations?filter=with_build_results`

`https://server.mycompany.com:20343/api/integrations?filter=with_build_results&last=15`

`https://server.mycompany.com:20343/api/integrations?last=1`

`https://server.mycompany.com:20343/api/integrations?last=1&summary_only=true`

`https://server.mycompany.com:20343/api/integrations?count=true`

__Parameters__

_filter_ (optional)

- Choices: `non_fatal`, `with_build_results`
- Type: `string`

_last_ (optional)

- The last specified number of integrations.
- Type: `number`

_count_ (optional)

- The total number of integrations.
- Type: `number`

_summary_only_ (optional)

- A Boolean value that indicates whether to return a brief summary instead of the regular payload.
- Type: `boolean`

__Response__: `200`

_Body_

1. `{`
2. `"count": 1,`
3. `"results": [`
4. `{`
5. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
6. `"_rev": "17-869fccee9b37638a719c20b1dcfa6869",`
7. `"number": 1,`
8. `"result": "succeeded",`
9. `"success_streak": 1,`
10. `"bot": {`
11. `...`
12. `},`
13. `"shouldClean": false,`
14. `"doc_type": "integration",`
15. `"currentStep": "completed",`
16. `"queuedDate": "2015-07-20T21:30:58.971Z",`
17. `"buildServiceFingerprint": "9C:67:D4:4A:00:97:0F:22:7B:B1:68:7E:28:1D:E0:5E:F2:E4:45:7C",`
18. `"startedTime": "2015-07-20T21:30:59.669Z",`
19. `"revisionBlueprint": {`
20. `...`
21. `},`
22. `"buildResultSummary": {`
23. `"analyzerWarningCount": 0,`
24. `"testFailureCount": 0,`
25. `"testsChange": 220,`
26. `"errorCount": 0,`
27. `"testsCount": 220,`
28. `"testFailureChange": 0,`
29. `"warningChange": 0,`
30. `"regressedPerfTestCount": 0,`
31. `"warningCount": 0,`
32. `"errorChange": 0,`
33. `"improvedPerfTestCount": 0,`
34. `"analyzerWarningChange": 0,`
35. `"codeCoveragePercentage": 0,`
36. `"codeCoveragePercentageDelta": 0`
37. `},`
38. `"endedTime": "2015-07-20T21:31:23.906Z",`
39. `"endedTimeDate": [`
40. `2015,`
41. `7,`
42. `20,`
43. `21,`
44. `31,`
45. `23,`
46. `906`
47. `],`
48. `"duration": 24.237,`
49. `"ccPercentage": 0,`
50. `"ccPercentageDelta": 0`
51. `}`
52. `]`
53. `}`

__Response__: `400`

_Body_

1. `{`
2. `"status": 400,`
3. `"message": "Filter 'foobar' is not supported"`
4. `}`

### Retrieving Tests for an Integration

__POST__

`/integrations/{id}/test/batch{?deviceIdentifier}`

Retrieves the tests for an integration. Optionally, you can specify the `deviceIdentifier` to filter the tests for the given device.

__Examples__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad/test/batch`

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad/test/batch?676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

_deviceIdentifier_ (optional)

- The device ID.
- Type: `string`
- Example: `676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64`

__Response__: `200`

_Body_

1. `{`
2. `"count": 2,`
3. `"results": [`
4. `{`
5. `"_id": "b31ad8317300e89b2db73aad3d049f7f",`
6. `"_rev": "1-37569504c8dee4e1de5e1ed5341833f6",`
7. `"perfMetrics": {},`
8. `"testableBlueprintName": "Sketch",`
9. `"passed": 1,`
10. `"path": [`
11. `"Sketch",`
12. `"SketchFileTests",`
13. `"testOpenFile"`
14. `],`
15. `"title": "testOpenFile",`
16. `"testedDevice": {`
17. `"osVersion": "10.11",`
18. `"connected": true,`
19. `"simulator": false,`
20. `"modelCode": "MacBookPro11,3",`
21. `"deviceType": "com.apple.mac",`
22. `"modelName": "MacBook Pro",`
23. `"revision": "3-824d6d3e1adedab99b103ab21f6b330d",`
24. `"modelUTI": "com.apple.macbookpro-15-retina-display",`
25. `"name": "server.mycompany.com",`
26. `"trusted": true,`
27. `"doc_type": "device",`
28. `"supported": true,`
29. `"processor": "2.5 GHz Intel Core i7",`
30. `"identifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
31. `"enabledForDevelopment": true,`
32. `"serialNumber": "XYZ",`
33. `"platformIdentifier": "com.apple.platform.macosx",`
34. `"ID": "b31ad8317300e89b2db73aad3d005719",`
35. `"architecture": "x86_64",`
36. `"retina": false,`
37. `"isServer": true`
38. `},`
39. `"date": [`
40. `2015,`
41. `7,`
42. `20`
43. `],`
44. `"deviceIdentifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
45. `"endTime": 2,`
46. `"keyPath": "Sketch.SketchFileTests.testOpenFile",`
47. `"doc_type": "test",`
48. `"failureSummaries": [],`
49. `"integration": "b31ad8317300e89b2db73aad3d049327",`
50. `"startTime": 1,`
51. `"dateISO8601": "2015-07-20T21:31:22.590Z",`
52. `"testableBlueprintPath": "Sketch.xcodeproj"`
53. `},`
54. `{`
55. `"_id": "b31ad8317300e89b2db73aad3d04a31c",`
56. `"_rev": "1-64fe6ec373b4e3075cc299cf411fe425",`
57. `"perfMetrics": {},`
58. `"testableBlueprintName": "Sketch",`
59. `"passed": 1,`
60. `"path": [`
61. `"Sketch",`
62. `"SketchFileTests",`
63. `"testOpenFile"`
64. `],`
65. `"title": "testOpenFile",`
66. `"testedDevice": {`
67. `"osVersion": "10.11",`
68. `"connected": true,`
69. `"simulator": false,`
70. `"modelCode": "MacBookPro11,3",`
71. `"deviceType": "com.apple.mac",`
72. `"modelName": "MacBook Pro",`
73. `"revision": "3-824d6d3e1adedab99b103ab21f6b330d",`
74. `"modelUTI": "com.apple.macbookpro-15-retina-display",`
75. `"name": "server.mycompany.com",`
76. `"trusted": true,`
77. `"doc_type": "device",`
78. `"supported": true,`
79. `"processor": "2.5 GHz Intel Core i7",`
80. `"identifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
81. `"enabledForDevelopment": true,`
82. `"serialNumber": "XYZ",`
83. `"platformIdentifier": "com.apple.platform.macosx",`
84. `"ID": "b31ad8317300e89b2db73aad3d005719",`
85. `"architecture": "x86_64",`
86. `"retina": false,`
87. `"isServer": true,`
88. `"tinyID": "6C69E42"`
89. `},`
90. `"date": [`
91. `2015,`
92. `7,`
93. `20`
94. `],`
95. `"deviceIdentifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
96. `"endTime": 2,`
97. `"keyPath": "Sketch.SketchFileTests.testOpenFile",`
98. `"doc_type": "test",`
99. `"failureSummaries": [],`
100. `"integration": "b31ad8317300e89b2db73aad3d049327",`
101. `"startTime": 1,`
102. `"dateISO8601": "2015-07-20T21:31:22.591Z",`
103. `"testableBlueprintPath": "Sketch.xcodeproj"`
104. `}`
105. `]`
106. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Retrieving Commits for an Integration

__GET__

`/integrations/{id}/commits`

Retrieves the test information list for a given integration and device identifier.

__Example__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad/commits`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `200`

_Body_

1. `{`
2. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
3. `"_rev": "3-7fda81759371fb8644058c0cfc83737e",`
4. `"commits": {`
5. `"6446FCB001D8C2E70EC59D119F3E3318109CE1A9": [`
6. `{`
7. `"XCSCommitCommitChangeFilePaths": [`
8. `{`
9. `"status": 4,`
10. `"filePath": "Sketch.xcodeproj/project.pbxproj"`
11. `},`
12. `{`
13. `"status": 1,`
14. `"filePath": "Sketch.xcodeproj/project.xcworkspace/xcshareddata/Sketch.xcscmblueprint"`
15. `},`
16. `{`
17. `"status": 1,`
18. `"filePath": "Sketch.xcodeproj/project.xcworkspace/xcshareddata/Sketch.xccheckout"`
19. `}`
20. `],`
21. `"XCSCommitMessage": "Remove run scripts (is obsolete and was causing a warning)",`
22. `"XCSBlueprintRepositoryID": "6446FCB001D8C2E70EC59D119F3E3318109CE1A9",`
23. `"XCSCommitContributor": {`
24. `"XCSContributorEmails": [`
25. `"appleseed@mycompany.com"`
26. `],`
27. `"XCSContributorName": "John Appleseed",`
28. `"XCSContributorDisplayName": "John Appleseed"`
29. `},`
30. `"XCSCommitHash": "3982fd5a6dd349c3673c9f91a96baf69eedc44a1",`
31. `"XCSCommitTimestamp": "2015-06-19T18:37:31.000Z",`
32. `"XCSCommitTimestampDate": [`
33. `2015,`
34. `6,`
35. `19,`
36. `18,`
37. `37,`
38. `31,`
39. `0`
40. `]`
41. `}`
42. `]`
43. `},`
44. `"integration": "b31ad8317300e89b2db73aad3d049327",`
45. `"botID": "b31ad8317300e89b2db73aad3d048d19",`
46. `"endedTimeDate": [`
47. `2015,`
48. `7,`
49. `20,`
50. `21,`
51. `31,`
52. `1,`
53. `830`
54. `],`
55. `"doc_type": "commit"`
56. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Retrieving Issues for an Integration

__GET__

`/integrations/{id}/issues`

Retrieves the test information list of issues for a given integration and device identifier.

__Example__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad/issues`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `200`

_Body_

1. `{`
2. `"buildServiceErrors": [],`
3. `"buildServiceWarnings": [],`
4. `"triggerErrors": [],`
5. `"errors": {`
6. `"unresolvedIssues": [],`
7. `"freshIssues": [`
8. `{`
9. `"_id": "37f997baa062fc9576f80f117b0244db",`
10. `"_rev": "3-e22d523aaaefcba794ee958184008f65",`
11. `"message": "Cannot assign a value of type 'String' to a value of type 'Int'",`
12. `"type": "error",`
13. `"issueType": "Swift Compiler Error",`
14. `"commits": [`
15. `{`
16. `"XCSCommitCommitChangeFilePaths": [`
17. `{`
18. `"status": 4,`
19. `"filePath": "testing-app/XMCStock.swift"`
20. `}`
21. `],`
22. `"XCSCommitMessage": "Forcing an error on purpose to test issues",`
23. `"XCSBlueprintRepositoryID": "090F3C64B0F773799E72487C8CB2AA2DCE01DCAA",`
24. `"XCSCommitContributor": {`
25. `"XCSContributorEmails": [`
26. `"jappleseed@mycompany.com"`
27. `],`
28. `"XCSContributorName": "John Appleseed",`
29. `"XCSContributorDisplayName": "John Appleseed"`
30. `},`
31. `"XCSCommitHash": "ea0e20d780a36d49003dcbc5e65592cf24a097db",`
32. `"XCSCommitTimestamp": "2015-07-24T02:06:17.000Z"`
33. `}`
34. `],`
35. `"target": "testing-app",`
36. `"documentFilePath": "DojoTesting/testing-app/XMCStock.swift",`
37. `"documentLocationData": "...",`
38. `"lineNumber": 19,`
39. `"integrationID": "b31ad8317300e89b2db73aad3d0194ad",`
40. `"age": 0,`
41. `"status": 0`
42. `}`
43. `],`
44. `"resolvedIssues": [],`
45. `"silencedIssues": []`
46. `},`
47. `"warnings": {`
48. `"unresolvedIssues": [],`
49. `"freshIssues": [],`
50. `"resolvedIssues": [],`
51. `"silencedIssues": []`
52. `},`
53. `"testFailures": {`
54. `"unresolvedIssues": [],`
55. `"freshIssues": [],`
56. `"resolvedIssues": [],`
57. `"silencedIssues": []`
58. `},`
59. `"analyzerWarnings": {`
60. `"unresolvedIssues": [],`
61. `"freshIssues": [],`
62. `"resolvedIssues": [],`
63. `"silencedIssues": []`
64. `}`
65. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

### Retrieving Files for an Integration

__GET__

`/integrations/{id}/files`

Retrieves the list of files for a given integration. The results property contains entries for:

- xcodebuild result bundle (zip)
- build service log
- xcodebuild log
- source control log
- session log

__Example__

`https://server.mycompany.com:20343/api/integrations/b31ad8317300e89b2db73aad3d0194ad/files`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

__Response__: `200`

_Body_

1. `{`
2. `/* The number of files */`
4. `"count": 5,`
6. `/* The list of files associated with the integration */`
7. `"results": [`
8. `{`
9. `/* Whether the file can be downloaded anonymously */`
10. `"allowAnonymousAccess": false,`
12. `/* The size of the file (in bytes) */`
13. `"size": 528254,`
15. `/* The name of the file */`
16. `"fileName": "xcodebuild_result.bundle.zip",`
18. `/* The associated integration ID */`
19. `"integrationID": "bb5b5dfa1c4abff347d28bed7e00bf87",`
21. `/* The relative path */`
22. `"relativePath": "bb5b5dfa1c4abff347d28bed7e00b381-Sketch/1/xcodebuild_result.bundle.zip"`
23. `}`
24. `...`
25. `...`
26. `]`
27. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "Integration not found"`
4. `}`

###

[Bots](Bots.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmrnknltc)

[Assets](Assets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnbnknltc)

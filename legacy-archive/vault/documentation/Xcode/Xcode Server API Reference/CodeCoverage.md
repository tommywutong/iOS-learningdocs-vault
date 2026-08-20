---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/CodeCoverage.html
archived_at: '2026-07-18T02:24:23.004090Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Code Coverage

Integrations that run tests can optionally generate code coverage information, which measures which parts of your codebase are being run by your tests.

### Retrieving Code Coverage for an Integration

__GET__

`/integration/{id}/coverage{?include_methods}`

Retrieves the Code Coverage information for a given integration. Code Coverage information is stored hierarchically. From top to bottom, an integration contains one or more targets, each target contains files and files contain methods. Each method contains device-specific coverage:

- integration ID

  - target

    - file

      - method

        - device A
        - device B
        - …

The default behavior (i.e. `/integration/b31ad8317300e89b2db73aad3d0194ad/coverage`) retrieves the entire tree, and is the same as invoking it with `include_methods=true`. If `include_methods=false` is specified, only `target` and `file` coverage is returned.

__Examples__

`https://server.mycompany.com:20343/api/integration/b31ad8317300e89b2db73aad3d0194ad/coverage`

`https://server.mycompany.com:20343/api/integration/b31ad8317300e89b2db73aad3d0194ad/coverage?include_methods=true`

`https://server.mycompany.com:20343/api/integration/b31ad8317300e89b2db73aad3d0194ad/coverage?include_methods=false`

__Parameters__

_id_ (required)

- The integration ID.
- Type: `string`
- Example: `b31ad8317300e89b2db73aad3d0194ad`

_include_methods_ (optional)

- If `true`, all available coverage data is returned. If `false`, only `target` and `file` coverage data is returned, excluding file methods.
- Type: `boolean`

__Request__: `/integration/b31ad8317300e89b2db73aad3d0194ad/coverage`

__Response__: `200`

_Body_

1. `{`
2. `"trg": {`
3. `"Sketch": {`
4. `"fls": {`
5. `"SKUIController.m": {`
6. `"lnpd": 0,`
7. `"cnt": 2,`
8. `"tte": "SKUIController.m",`
9. `"lnp": 50,`
10. `"dvcs": [`
11. `{`
12. `"dvc": "E82BDC1",`
13. `"lnp": 50,`
14. `"lnpd": 0`
15. `}`
16. `],`
17. `"mth": [`
18. `{`
19. `"tte": "+[SKUIController fileWithPath:]",`
20. `"dvcs": [`
21. `{`
22. `"dvc": "E82BDC1",`
23. `"lnp": 50,`
24. `"lnpd": 0`
25. `}`
26. `],`
27. `"lnp": 50,`
28. `"lnpd": 0`
29. `},`
30. `{`
31. `"tte": "-[SKUIController initWithPath:]",`
32. `"dvcs": [`
33. `{`
34. `"dvc": "E82BDC1",`
35. `"lnp": 75,`
36. `"lnpd": 0`
37. `}`
38. `],`
39. `"lnp": 50,`
40. `"lnpd": 12`
41. `}`
42. `]`
43. `}`
44. `},`
45. `"dvcs": [`
46. `{`
47. `"dvc": "E82BDC1",`
48. `"lnp": 50,`
49. `"lnpd": 0`
50. `}`
51. `],`
52. `"cnt": 2,`
53. `"lnp": 50,`
54. `"lnpd": 0`
55. `}`
56. `},`
57. `"dvcs": [`
58. `{`
59. `"osVersion": "10.11",`
60. `"connected": true,`
61. `"simulator": false,`
62. `"modelCode": "MacBookPro11,3",`
63. `"deviceType": "com.apple.mac",`
64. `"modelName": "MacBook Pro",`
65. `"revision": "3-57fbd763eaee716c31707cd0623c099e",`
66. `"modelUTI": "com.apple.macbookpro-15-retina-display",`
67. `"name": "XcodeServer Mac",`
68. `"trusted": true,`
69. `"doc_type": "device",`
70. `"supported": true,`
71. `"processor": "2.5 GHz Intel Core i7",`
72. `"identifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
73. `"enabledForDevelopment": true,`
74. `"serialNumber": "XYZ",`
75. `"platformIdentifier": "com.apple.platform.macosx",`
76. `"ID": "5764488b58526c86cab94e981d0034ed",`
77. `"architecture": "x86_64",`
78. `"retina": false,`
79. `"isServer": true`
80. `}`
81. `],`
82. `"integrationID": "5764488b58526c86cab94e981d00dac1",`
83. `"integrationNumber": 3,`
84. `"lnp": 50,`
85. `"lnpd": 12`
86. `}`

__Request__: `/integration/b31ad8317300e89b2db73aad3d0194ad/coverage?include_methods=false`

__Response__: `200`

_Body_

1. `{`
2. `"trg": {`
3. `"Sketch": {`
4. `"fls": {`
5. `"SKUIController.m": {`
6. `"lnpd": 0,`
7. `"cnt": 2,`
8. `"tte": "SKUIController.m",`
9. `"lnp": 50,`
10. `"dvcs": [`
11. `{`
12. `"dvc": "E82BDC1",`
13. `"lnp": 30.45007032348804,`
14. `"lnpd": 0`
15. `}`
16. `]`
17. `}`
18. `},`
19. `"dvcs": [`
20. `{`
21. `"dvc": "E82BDC1",`
22. `"lnp": 60.57347670250897,`
23. `"lnpd": 0`
24. `}`
25. `],`
26. `"cnt": 1,`
27. `"lnp": 50,`
28. `"lnpd": 0`
29. `}`
30. `},`
31. `"dvcs": [`
32. `{`
33. `"osVersion": "10.11",`
34. `"connected": true,`
35. `"simulator": false,`
36. `"modelCode": "MacBookPro11,3",`
37. `"deviceType": "com.apple.mac",`
38. `"modelName": "MacBook Pro",`
39. `"revision": "3-57fbd763eaee716c31707cd0623c099e",`
40. `"modelUTI": "com.apple.macbookpro-15-retina-display",`
41. `"name": "XcodeServer Mac",`
42. `"trusted": true,`
43. `"doc_type": "device",`
44. `"supported": true,`
45. `"processor": "2.5 GHz Intel Core i7",`
46. `"identifier": "676EE417-E15F-50DF-9D20-525B7E3F13CE-x86_64",`
47. `"enabledForDevelopment": true,`
48. `"serialNumber": "XYZ",`
49. `"platformIdentifier": "com.apple.platform.macosx",`
50. `"ID": "5764488b58526c86cab94e981d0034ed",`
51. `"architecture": "x86_64",`
52. `"retina": false,`
53. `"isServer": true`
54. `}`
55. `],`
56. `"integrationID": "5764488b58526c86cab94e981d00dac1",`
57. `"integrationNumber": 3,`
58. `"lnp": 50,`
59. `"lnpd": 12`
60. `}`

__Response__: `400`

_Body_

1. `{`
2. `"status": 400,`
3. `"message": "Filter 'foobar' is not supported"`
4. `}`

__Response__: `404`

_Body_

1. `{`
2. `"status": 404,`
3. `"message": "integration not found"`
4. `}`

[Assets](Assets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnbnknltc)

[Schema](Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnrnknltc)

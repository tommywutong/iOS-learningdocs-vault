---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/Schema.html
archived_at: '2026-07-18T02:24:25.554668Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Schema

The Xcode Server API consumes and produces JSON objects. Each type of object the Xcode Server uses has a defined structure, with certain expected properties.

> [!IMPORTANT]
> 

### Bot

1. `{`
2. `/* Bot ID */`
3. `"_id": "bb5b5dfa1c4abff347d28bed7e00b381",`
5. `/* Revision ID */`
6. `"_rev": "5-a050220837762e423ee28a5e9c150844",`
8. `/* Configuration. See the section "Schema > Bot Configuration" for more information. */`
9. `"configuration": {`
10. `...`
11. `},`
13. `/* Name of the bot */`
14. `"name": "Sketch",`
16. `/* The integration counter`
17. `This number dictates the number that the next integration will be set to.`
18. `*/`
19. `"integration_counter": 2,`
21. `/* The document type */`
22. `"doc_type": "bot",`
24. `/* Last revision blueprint. See the section "Blueprint" for more information. */`
25. `"lastRevisionBlueprint": {`
26. `...`
27. `}`
28. `}`

### Bot Configuration

1. `{`
2. `/* ----- Scheduling ----- */`
4. `/* Schedule type:`
5. `1: Periodically`
6. `2: On commit`
7. `3: Manual`
8. `*/`
9. `"scheduleType": 3,`
11. `/* Periodic schedule`
12. `1: Hourly`
13. `2: Daily`
14. `3: Weekly`
15. `Dependencies:`
16. `- 'scheduleType' set to 1 (Periodically)`
17. `*/`
18. `"periodicScheduleInterval": 0,`
20. `/* Minutes after the hour to integrate`
21. `Value: 0 to 59`
22. `Dependencies:`
23. `- 'periodicScheduleInterval' set to 1 (Hourly)`
24. `"minutesAfterHourToIntegrate": 0,`
26. `/* Hour of integration`
27. `Value: 0 (midnight) to 23`
28. `Dependencies:`
29. `- 'periodicScheduleInterval' set to 2 (Daily) or 3 (Weekly)`
30. `*/`
31. `"hourOfIntegration": 0,`
33. `/* Weekly schedule day`
34. `1: Monday`
35. `2: Tuesday`
36. `3: Wednesday`
37. `4: Thursday`
38. `5: Friday`
39. `6: Saturday`
40. `7: Sunday`
41. `Dependencies:`
42. `- 'periodicScheduleInterval' set to 3 (Weekly)`
43. `"weeklyScheduleDay": 0,`
45. `/* ----- General ----- */`
47. `/* Scheme name`
48. `The name of the scheme used to integrate.`
49. `*/`
50. `"schemeName": "dojo-testing",`
52. `/* Built from clean`
53. `0: Never`
54. `1: Always`
55. `2: Once a day`
56. `3: Once a week`
57. `*/`
58. `"builtFromClean": 0,`
60. `/* Configuration`
61. `Value: "Debug" | "Release" | "XXX" <- we need to set the value because if exists already,`
62. `devs cannot remove it (there is no support for it)`
63. `*/`
64. `"buildConfiguration": "Release",`
66. `/* ----- Actions ----- */`
68. `/* Performs analyze action`
69. `Value: true | false`
70. `*/`
71. `"performsAnalyzeAction": true,`
73. `/* Performs test action`
74. `Value: true | false`
75. `*/`
76. `"performsTestAction": true,`
78. `/* Performs archive action`
79. `Value: true | false`
80. `*/`
81. `"exportsProductFromArchive": true,`
83. `/* ----- Testing ----- */`
85. `/* Code coverage`
86. `1: Use scheme setting`
87. `2: Enabled`
88. `3: Disabled`
89. `Dependencies:`
90. `- 'performsTestAction' set to true`
91. `*/`
92. `"codeCoveragePreference": 1,`
94. `/* ----- Triggers ----- */`
96. `/* Triggers`
97. `Value: array of <Trigger>`
98. `Trigger:`
99. `phase: 1 (Before) | 2 (After)`
100. `scriptBody: string (script)`
101. `type:`
102. `name: string (title of the script)`
103. `conditions:`
104. `status: ???`
105. `onWarnings: true | false`
106. `onBuildErrors: true | false`
107. `onInternalErrors: true | false`
108. `onAnalyzerWarnings: true | false`
109. `onFailingTests: true | false`
110. `onSuccess: true | false`
111. `Dependencies:`
112. `- 'phase' set to 2 must specify Trigger property 'conditions'.`
113. `*/`
114. `"triggers": [`
115. `...`
116. `],`
118. `/* ----- Devices ----- */`
120. `/* Device specification`
121. `Value: array of <device ID>`
122. `Dependencies:`
123. `- 'performsTestAction' set to true`
124. `*/`
125. `"deviceSpecification": {`
126. `"filters": [`
127. `{`
128. `...`
129. `],`
130. `"deviceIdentifiers": [`
131. `...`
132. `]`
133. `},`
135. `/* ----- Blueprint ----- */`
137. `"sourceControlBlueprint": {`
138. `/* Unique identifier for each blueprint`
139. `Value: A valid UUID`
140. `*/`
141. `"DVTSourceControlWorkspaceBlueprintIdentifierKey": "34D1C3F9-E33F-4935-A5E4-7154F4309EDF",`
143. `/* Locations`
144. `Value: array of <Location>`
145. `Location:`
146. `DVTSourceControlBranchIdentifierKey: string (branch name)`
147. `DVTSourceControlBranchOptionsKey:`
148. `4 (normal remote branch) |`
149. `5 (primary remote branch, necessary for trunk-like branch in Subversion)`
150. `DVTSourceControlPathIdentifierKey: string (relative path in repository)`
151. `DVTSourceControlLocationRevisionKey: string (revision)`
152. `DVTSourceControlWorkspaceBlueprintLocationTypeKey: one of the following options:`
153. `"DVTSourceControlBranch" (Branch)`
154. `"DVTSourceControlPathLocation" (Path, Subversion-only)`
155. `"DVTSourceControlLockedRevisionLocation" (Revision, Git-only)`
156. `*/`
157. `"DVTSourceControlWorkspaceBlueprintLocationsKey": {`
158. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
159. `"DVTSourceControlBranchIdentifierKey": "master",`
160. `"DVTSourceControlBranchOptionsKey": 5,`
161. `"DVTSourceControlWorkspaceBlueprintLocationTypeKey": "DVTSourceControlBranch"`
162. `}`
163. `},`
165. `/* The name for the blueprint, typically the name of the Xcode project or workspace`
166. `Value: string`
167. `*/`
168. `"DVTSourceControlWorkspaceBlueprintNameKey": "Project",`
170. `/* The identifier of the working copy containing the Xcode project or workspace to build,`
171. `considered the primary working copy.`
172. `Value: string (repository identifier)`
173. `*/`
174. `"DVTSourceControlWorkspaceBlueprintPrimaryRemoteRepositoryKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
176. `/* The relative path in the primary working copy to the Xcode project or workspace to build`
177. `Value: string (relative path)`
178. `*/`
179. `"DVTSourceControlWorkspaceBlueprintRelativePathToProjectKey": "Project.xcworkspace",`
181. `/* Repositories`
182. `Value: array of <Repository>`
183. `Repository:`
184. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey: true | false`
185. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustSelfSignedCertKey: true | false`
186. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey: string`
187. `DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey:`
188. `"com.apple.dt.Xcode.sourcecontrol.Git" (Git) |`
189. `"com.apple.dt.Xcode.sourcecontrol.Subversion" (Subversion)`
190. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey: a string of one of the following fingerprint options:`
191. `RSA (SSH servers) |`
192. `MD5 (self-signed SSL server certificates)`
193. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey: string (URI)`
194. `*/`
195. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoriesKey": [`
196. `{`
197. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey": true,`
198. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
199. `"DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey": "com.apple.dt.Xcode.sourcecontrol.Git",`
200. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey": "174F678B9ED220D9C8B2A47F42392A44",`
201. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey": "git@server:/repo.git"`
202. `}`
203. `],`
205. `/* Authentication strategies`
206. `Value: dictionary of string (repository identifier) to <Authentication>`
207. `Authentication:`
208. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey: one of the following options:`
209. `"DVTSourceControlAuthenticationStrategy" (Anonymous)`
210. `"DVTSourceControlBasicAuthenticationStrategy" (Username and Password)`
211. `"DVTSourceControlSSHKeysAuthenticationStrategy" (SSH Keys)`
212. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey: string (Password or Passphrase)`
213. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey: string (Username)`
214. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey: string (Base64-encoded public key data)`
215. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey: string (Base64-encoded private key data)`
216. `*/`
217. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationStrategiesKey": {`
218. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
219. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey":`
220. `"DVTSourceControlBasicAuthenticationStrategy",`
221. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey": "foobar",`
222. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey": "git"`
223. `}`
224. `},`
226. `/* The blueprint format version`
227. `Value: 204`
228. `*/`
229. `"DVTSourceControlWorkspaceBlueprintVersion": 204,`
231. `/* Working copy layout`
232. `Value: dictionary of string (repository identifier) to string (relative path of checkout)`
233. `*/`
234. `"DVTSourceControlWorkspaceBlueprintWorkingCopyPathsKey": {`
235. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": "Project/"`
236. `}`
237. `}`
238. `}`

### Integration

1. `{`
2. `/* Integration ID */`
3. `"_id": "bb5b5dfa1c4abff347d28bed7e00bf87",`
5. `/* Revision ID */`
6. `"_rev": "17-c23a1a6231571d17435af0f0ff1f4228",`
8. `/* Integration number */`
9. `"number": 1,`
11. `/* The result of the integration`
12. `Values:`
13. `succeeded`
14. `test-failures`
15. `build-errors`
16. `warnings`
17. `analyzer-warnings`
18. `build-failed`
19. `checkout-error`
20. `internal-error`
21. `internal-checkout-error`
22. `internal-build-error`
23. `internal-processing-error`
24. `canceled`
25. `trigger-error`
26. `unknown`
27. `*/`
28. `"result": "succeeded",`
30. `/* The number of successful continuous integrations */`
31. `"success_streak": 1,`
33. `/* The bot snapshot. See the section "Schema > Bot" for more information. */`
34. `"bot": {`
35. `...`
36. `},`
38. `/* */`
39. `"shouldClean": false,`
41. `/* The document type */`
42. `"doc_type": "integration",`
44. `/* The current step of the integration */`
45. `"currentStep": "completed",`
47. `/* The date when the integration was triggered */`
48. `"queuedDate": "2015-08-03T17:26:53.183Z",`
50. `/* The date when the integration started */`
51. `"startedTime": "2015-08-03T17:26:53.786Z",`
53. `/* The date when the integration finished */`
54. `"endedTime": "2015-08-03T17:27:15.050Z",`
56. `/* The duration of the integration (in seconds) */`
57. `"duration": 21.264,`
59. `/* Revision blueprint. See the section "Blueprint" for more information. */`
60. `"revisionBlueprint": {`
61. `...`
62. `},`
64. `/* The build results summary`
65. `Values:`
66. `errorCount: number of errors detected in the Build phase`
67. `errorChange: number of errors delta with the previous integration`
68. `warningCount: number of warnings detected in the Build phase`
69. `warningChange: number of warnings delta with the previous integration`
70. `analyzerWarningCount: number of warnings detected in the Analysis phase`
71. `analyzerWarningChange: number of warnings delta with the previous integration`
72. `testsCount: number of tests to be executed`
73. `testsChange: number of tests delta with the previous integration`
74. `testFailureCount: number of failed tests`
75. `testFailureChange: number of failed tests delta with the previous integration`
76. `regressedPerfTestCount: number of regressed performance tests`
77. `improvedPerfTestCount: number of improved performance tests`
78. `codeCoveragePercentage: coverage percentage`
79. `codeCoveragePercentageDelta: coverage percentage delta with the previous integration`
80. `*/`
81. `"buildResultSummary": {`
82. `"errorCount": 0,`
83. `"errorChange": 0,`
84. `"warningCount": 0,`
85. `"warningChange": 0,`
86. `"analyzerWarningCount": 0,`
87. `"analyzerWarningChange": 0,`
88. `"testsCount": 220,`
89. `"testsChange": 220,`
90. `"testFailureCount": 0,`
91. `"testFailureChange": 0,`
92. `"regressedPerfTestCount": 0,`
93. `"improvedPerfTestCount": 0,`
94. `"codeCoveragePercentage": 71,`
95. `"codeCoveragePercentageDelta": 0`
96. `}`
97. `}`

### Issue

1. `{`
2. `/*`
3. `The top-level properties are the following:`
5. `errors`
6. `testFailures`
7. `analyzerWarnings`
8. `warnings`
9. `buildServiceErrors`
10. `buildServiceWarnings`
12. `Each of these properties (except for buildServiceErrors and buildServiceWarnings) contains the following sub-properties:`
14. `freshIssues: new issues that appeared in the integration`
15. `unresolvedIssues: issues that appeared before and have not been resolved yet`
16. `resolvedIssues: issues that appeared before and have been resolved`
18. `Each of these sub-properties are arrays containing one or more elements with the following structure`
19. `{`
20. `/* Issue status`
21. `0: New`
22. `1: Unresolved`
23. `2: Resolved`
24. `*/`
25. `"status": 1,`
27. `/* The document file path`
28. `Under some circumstances, the file may not exist (i.e. the issue is a test failure).`
29. `*/`
30. `"documentFilePath": "<unknown>",`
32. `/* The name of the test */`
33. `"testCase": "-[TestKVOConditionValidator testAsyncCallback]",`
35. `/* The reason for the issue */`
36. `"message": "Test process exited unexpectedly.",`
38. `/* The associated integration ID where this issue was first discovered */`
39. `"integrationID": "ee61c2f211a21ebd39d697f056924f2d",`
41. `/* Number of integrations since the issue appeared */`
42. `"age": 5,`
44. `/* Issue type`
45. `Values:`
46. `error`
47. `warning`
48. `analyzerWarning`
49. `testFailure`
50. `buildServiceError`
51. `buildServiceWarning`
52. `triggerError`
53. `unknown`
54. `*/`
55. `"type": "testFailure",`
57. `/* A list of commits associated with the integration. See the section "Schema > Commit" for more information. */`
58. `"commits": [`
60. `]`
61. `}`
62. `*/`
64. `/* Issue ID */`
65. `"_id": "0c613a043b42f4ff8ee13ef6c61abe9a",`
67. `/* revision ID */`
68. `"_rev": "3-339372917d7245edf03ae553db9f7f89",`
70. `"errors": {`
71. `"unresolvedIssues": [`
73. `],`
74. `"resolvedIssues": [`
76. `],`
77. `"freshIssues": [`
79. `]`
80. `},`
81. `"testFailures": {`
82. `"unresolvedIssues": [`
84. `],`
85. `"resolvedIssues": [`
87. `],`
88. `"freshIssues": [`
90. `]`
91. `},`
92. `"buildServiceWarnings": [`
94. `],`
95. `"analyzerWarnings": {`
96. `"unresolvedIssues": [`
98. `],`
99. `"resolvedIssues": [`
101. `],`
102. `"freshIssues": [`
104. `]`
105. `},`
106. `"buildServiceErrors": [`
108. `],`
109. `"warnings": {`
110. `"unresolvedIssues": [`
112. `],`
113. `"resolvedIssues": [`
115. `],`
116. `"freshIssues": [`
118. `]`
119. `},`
121. `/* Integration ID */`
122. `"integration": "b76633a9c3974e21c2f263f6849ecf60",`
124. `/* The document type */`
125. `"doc_type": "issue"`
126. `}`

### Commit List

1. `{`
2. `/* Commit ID */`
3. `"_id": "b31ad8317300e89b2db73aad3d0194ad",`
5. `/* Revision ID */`
6. `"_rev": "3-7fda81759371fb8644058c0cfc83737e",`
8. `/* The list of commits per repository */`
9. `"commits": {`
11. `/* Repository ID (matched against the bot blueprint) */`
12. `"6446FCB001D8C2E70EC59D119F3E3318109CE1A9": [`
13. `{`
14. `/* A list of commits objects. See the section "Schema > Commit" for more information. */`
15. `}`
16. `]`
17. `},`
19. `/* Integration ID */`
20. `"integration": "b31ad8317300e89b2db73aad3d049327",`
22. `/* Bot ID */`
23. `"botID": "b31ad8317300e89b2db73aad3d048d19",`
25. `/* The document type */`
26. `"doc_type": "commit"`
27. `}`

### Commit

1. `{`
2. `/* List of file paths and SCM file status`
3. `File status codes:`
4. `1: Added`
5. `2: Deleted`
6. `4: Modified`
7. `8: Modified Properties`
8. `*/`
9. `"XCSCommitCommitChangeFilePaths": [`
10. `{`
11. `/* SCM status */`
12. `"status": 4,`
13. `"filePath": "Sketch.xcodeproj/project.pbxproj"`
14. `}`
15. `],`
17. `/* Commit message */`
18. `"XCSCommitMessage": "Remove run scripts (is obsolete and was causing a warning)",`
20. `/* Blueprint repository ID */`
21. `"XCSBlueprintRepositoryID": "6446FCB001D8C2E70EC59D119F3E3318109CE1A9",`
23. `/* Commit contributor list */`
24. `"XCSCommitContributor": {`
26. `/* List of emails associated with the user */`
27. `"XCSContributorEmails": [`
28. `"appleseed@mycompany.com"`
29. `],`
31. `/* Name of the contributor */`
32. `"XCSContributorName": "John Appleseed",`
34. `/* Display name of the contributor */`
35. `"XCSContributorDisplayName": "John Appleseed"`
36. `},`
38. `/* Commit hash */`
39. `"XCSCommitHash": "3982fd5a6dd349c3673c9f91a96baf69eedc44a1",`
41. `/* Commit timestamp */`
42. `"XCSCommitTimestamp": "2015-06-19T18:37:31.000Z"`
43. `}`

[Code Coverage](CodeCoverage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnjnknltc)

[Blueprint](Blueprint.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnznknltc)

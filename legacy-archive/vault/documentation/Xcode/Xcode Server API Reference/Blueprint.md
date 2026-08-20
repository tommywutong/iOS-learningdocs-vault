---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/Blueprint.html
archived_at: '2026-07-18T02:24:22.091354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Server API Reference](index.md)



## Blueprint

A blueprint is a set of instructions telling the bot what to check out and how. It provides the URIs for all repositories to check out files from, the branch to check out, the relative layout on disk, and the relative location of the project or workspace to build out of. It also can include the authentication information to use when checking out, although this information is sent only to the server and is never returned from it. Additionally, if a bot already has authentication information, it is merged into new blueprints provided where it is missing when the bot is being patched. Blueprints allow for representing arbitrarily complex check out scenarios and the examples here show how to construct authenticated ones for a single Git repository, a workspace that checks out files from two repositories and a single Subversion repository.

### Simple Git Example

1. `{`
2. `/* Unique identifier for each blueprint`
3. `Value: A valid UUID`
4. `*/`
5. `"DVTSourceControlWorkspaceBlueprintIdentifierKey": "34D1C3F9-E33F-4935-A5E4-7154F4309EDF",`
6. `/* Locations`
7. `Value: dictionary of string (repository identifier) to <Location>`
8. `Location:`
9. `Required:`
10. `DVTSourceControlWorkspaceBlueprintLocationTypeKey:`
11. `"DVTSourceControlBranch" (Branch) |`
12. `"DVTSourceControlLockedRevisionLocation" (Detached Head)`
13. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlBranch:`
14. `DVTSourceControlBranchIdentifierKey: string (branch name)`
15. `DVTSourceControlBranchOptionsKey:`
16. `4 (normal remote branch) |`
17. `5 (primary remote branch)`
18. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlLockedRevisionLocation:`
19. `DVTSourceControlLocationRevisionKey: string (revision hash)`
20. `*/`
21. `"DVTSourceControlWorkspaceBlueprintLocationsKey": {`
22. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
23. `"DVTSourceControlBranchIdentifierKey": "master",`
24. `"DVTSourceControlBranchOptionsKey": 5,`
25. `"DVTSourceControlWorkspaceBlueprintLocationTypeKey": "DVTSourceControlBranch"`
26. `}`
27. `},`
28. `/* The name for the blueprint, typically the name of the Xcode project or workspace`
29. `Value: string`
30. `*/`
31. `"DVTSourceControlWorkspaceBlueprintNameKey": "Project",`
32. `/* The identifier of the working copy containing the Xcode project or workspace to build, considered the primary working copy`
33. `Value: string (repository identifier)`
34. `*/`
35. `"DVTSourceControlWorkspaceBlueprintPrimaryRemoteRepositoryKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
36. `/* The relative path in the primary working copy to the Xcode project or workspace to build`
37. `Value: string (relative path)`
38. `*/`
39. `"DVTSourceControlWorkspaceBlueprintRelativePathToProjectKey": "Project.xcworkspace",`
40. `/* Repositories`
41. `Value: array of <Repository>`
42. `Repository:`
43. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey: true (requied)`
44. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey: string (consistent identifier within blueprint)`
45. `DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey: "com.apple.dt.Xcode.sourcecontrol.Git" (Git)`
46. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey: a string of one of the following fingerprint options:`
47. `RSA (SSH servers) |`
48. `MD5 (self-signed SSL server certificates)`
49. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey: string (URI)`
50. `*/`
51. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoriesKey": [`
52. `{`
53. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey": true,`
54. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
55. `"DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey": "com.apple.dt.Xcode.sourcecontrol.Git",`
56. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey": "174F678B9ED220D9C8B2A47F42392A44",`
57. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey": "git@server:/repo.git"`
58. `}`
59. `],`
60. `/* Authentication Strategies`
61. `Value: dictionary of string (repository identifier) to <Authentication>`
62. `Authentication:`
63. `Required:`
64. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey:`
65. `"DVTSourceControlAuthenticationStrategy" (Anonymous) |`
66. `"DVTSourceControlBasicAuthenticationStrategy" (Username and Password) |`
67. `"DVTSourceControlSSHKeysAuthenticationStrategy" (SSH Keys)`
68. `Required only for DVTSourceControlBasicAuthenticationStrategy and DVTSourceControlSSHKeysAuthenticationStrategy:`
69. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey: string (Password or Passphrase)`
70. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey: string (Username)`
71. `Required only for DVTSourceControlSSHKeysAuthenticationStrategy:`
72. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey: string (Base64-encoded public key data)`
73. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey: string (Base64-encoded private key data)`
74. `*/`
75. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationStrategiesKey": {`
76. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
77. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey": "DVTSourceControlBasicAuthenticationStrategy",`
78. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey": "foobar",`
79. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey": "git"`
80. `}`
81. `},`
82. `/* The blueprint format version`
83. `Value: 204`
84. `*/`
85. `"DVTSourceControlWorkspaceBlueprintVersion": 204,`
86. `/* Working Copy Layout`
87. `Value: dictionary of string (repository identifier) to string (relative path of checkout)`
88. `*/`
89. `"DVTSourceControlWorkspaceBlueprintWorkingCopyPathsKey": {`
90. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": "Project/"`
91. `},`
92. `}`

### Multi Repository Example

1. `{`
2. `/* Unique identifier for each blueprint`
3. `Value: A valid UUID`
4. `*/`
5. `"DVTSourceControlWorkspaceBlueprintIdentifierKey": "7A06494E-53C9-403D-9C19-ECB73D64AD28",`
6. `/* Locations`
7. `Value: dictionary of string (repository identifier) to <Location>`
8. `Location:`
9. `Required:`
10. `DVTSourceControlWorkspaceBlueprintLocationTypeKey:`
11. `"DVTSourceControlBranch" (Branch) |`
12. `"DVTSourceControlPathLocation" (Path, Subversion-only) |`
13. `"DVTSourceControlLockedRevisionLocation" (Revision, Git-only)`
14. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlBranch:`
15. `DVTSourceControlBranchIdentifierKey: string (branch name)`
16. `DVTSourceControlBranchOptionsKey:`
17. `4 (normal remote branch) |`
18. `5 (primary remote branch)`
19. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlLockedRevisionLocation:`
20. `DVTSourceControlLocationRevisionKey: string (revision hash)`
21. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlPathLocation:`
22. `DVTSourceControlPathIdentifierKey: string (relative path in repository)`
23. `*/`
24. `"DVTSourceControlWorkspaceBlueprintLocationsKey": {`
25. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
26. `"DVTSourceControlBranchIdentifierKey": "master",`
27. `"DVTSourceControlBranchOptionsKey": 5,`
28. `"DVTSourceControlWorkspaceBlueprintLocationTypeKey": "DVTSourceControlBranch"`
29. `},`
30. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": {`
31. `"DVTSourceControlBranchIdentifierKey": "trunk",`
32. `"DVTSourceControlBranchOptionsKey": 5,`
33. `"DVTSourceControlWorkspaceBlueprintLocationTypeKey": "DVTSourceControlBranch"`
34. `}`
35. `},`
36. `/* Working Copy Repository Locations`
37. `Value: dictionary of string (repository identifier) to <Branch and Tag Locations>`
38. `Branch and Tag Locations:`
39. `DVTSourceControlWorkingCopyRepositoryBranchesLocationKey: string (relative path in repository to branches folder)`
40. `DVTSourceControlWorkingCopyRepositoryTagsLocationKey: string (relative path in repository to tags folder)`
41. `DVTSourceControlWorkingCopyRepositoryPrimaryBranchLocationKey: string (relative path in repository to trunk folder)`
42. `*/`
43. `"DVTSourceControlWorkspaceBlueprintWorkingCopyRepositoryLocationsKey" : {`
44. `"34768997-536d-3cd6-3966-ce57b7db7bff" : {`
45. `"DVTSourceControlWorkingCopyRepositoryBranchesLocationKey" : "branches",`
46. `"DVTSourceControlWorkingCopyRepositoryTagsLocationKey" : "tags",`
47. `"DVTSourceControlWorkingCopyRepositoryPrimaryBranchLocationKey" : "trunk"`
48. `}`
49. `},`
50. `/* The name for the blueprint, typically the name of the Xcode project or workspace`
51. `Value: string`
52. `*/`
53. `"DVTSourceControlWorkspaceBlueprintNameKey": "MultiProject",`
54. `/* The identifier of the working copy containing the Xcode project or workspace to build, considered the primary working copy`
55. `Value: string (repository identifier)`
56. `*/`
57. `"DVTSourceControlWorkspaceBlueprintPrimaryRemoteRepositoryKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
58. `/* The relative path in the primary working copy to the Xcode project or workspace to build`
59. `Value: string (relative path)`
60. `*/`
61. `"DVTSourceControlWorkspaceBlueprintRelativePathToProjectKey": "MultiProject.xcworkspace",`
62. `/* Repositories`
63. `Value: array of <Repository>`
64. `Repository:`
65. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey: true (requied)`
66. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey: string (consistent identifier within blueprint)`
67. `DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey: "com.apple.dt.Xcode.sourcecontrol.Git" (Git)`
68. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey: a string of one of the following fingerprint options:`
69. `RSA (SSH servers) |`
70. `MD5 (self-signed SSL server certificates)`
71. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey: string (URI)`
72. `*/`
73. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoriesKey": [`
74. `{`
75. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey": true,`
76. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey": "47B0B4A0E6B2316DF0F333C188B6423A9479B516",`
77. `"DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey": "com.apple.dt.Xcode.sourcecontrol.Git",`
78. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey": "174F678B9ED220D9C8B2A47F42392A44",`
79. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey": "git@server:/multiproject.git"`
80. `},`
81. `{`
82. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey": true,`
83. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey": "360BCE85-D2C0-4DE1-937B-4A56E07173E6",`
84. `"DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey": "com.apple.dt.Xcode.sourcecontrol.Subversion",`
85. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey": "174F678B9ED220D9C8B2A47F42392A44",`
86. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey": "svn+ssh:\/\/server.example.com\/svn\/otherproject"`
87. `}`
88. `],`
89. `/* Authentication Strategies`
90. `Value: dictionary of string (repository identifier) to <Authentication>`
91. `Authentication:`
92. `Required:`
93. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey:`
94. `"DVTSourceControlAuthenticationStrategy" (Anonymous) |`
95. `"DVTSourceControlBasicAuthenticationStrategy" (Username and Password) |`
96. `"DVTSourceControlSSHKeysAuthenticationStrategy" (SSH Keys)`
97. `Required only for DVTSourceControlBasicAuthenticationStrategy and DVTSourceControlSSHKeysAuthenticationStrategy:`
98. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey: string (Password or Passphrase)`
99. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey: string (Username)`
100. `Required only for DVTSourceControlSSHKeysAuthenticationStrategy:`
101. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey: string (Base64-encoded public key data)`
102. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey: string (Base64-encoded private key data)`
103. `*/`
104. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationStrategiesKey": {`
105. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": {`
106. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey": "DVTSourceControlSSHKeysAuthenticationStrategy",`
107. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey": "MyPassphrase",`
108. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey": "me",`
109. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey": "c3NoLXJzYSBBQUFBQjNOemp...",`
110. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey": "LS0tLS1CRUdJTiBkFURSBLR..."`
111. `},`
112. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": {`
113. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey": "DVTSourceControlSSHKeysAuthenticationStrategy",`
114. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey": "MyPassphrase",`
115. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey": "me",`
116. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey": "c3NoLXJzYSBBQUFBQjNOemp...",`
117. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey": "LS0tLS1CRUdJTiBkFURSBLR..."`
118. `}`
119. `},`
120. `/* The blueprint format version`
121. `Value: 204`
122. `*/`
123. `"DVTSourceControlWorkspaceBlueprintVersion": 204,`
124. `/* Working Copy Layout`
125. `Value: dictionary of string (repository identifier) to string (relative path of checkout)`
126. `*/`
127. `"DVTSourceControlWorkspaceBlueprintWorkingCopyPathsKey": {`
128. `"47B0B4A0E6B2316DF0F333C188B6423A9479B516": "Project/",`
129. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": "OtherProject/"`
130. `},`
131. `}`

### Simple Subversion (svn) Example

1. `{`
2. `/* Unique identifier for each blueprint`
3. `Value: A valid UUID`
4. `*/`
5. `"DVTSourceControlWorkspaceBlueprintIdentifierKey": "D4124FDB-5D40-4170-9269-CAD0A6AB9493",`
6. `/* Locations`
7. `Value: dictionary of string (repository identifier) to <Location>`
8. `Location:`
9. `Required:`
10. `DVTSourceControlWorkspaceBlueprintLocationTypeKey:`
11. `"DVTSourceControlBranch" (Branch) |`
12. `"DVTSourceControlPathLocation" (Path)`
13. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlBranch:`
14. `DVTSourceControlBranchIdentifierKey: string (branch name)`
15. `DVTSourceControlBranchOptionsKey:`
16. `4 (normal remote branch) |`
17. `5 (primary remote branch, i.e. trunk)`
18. `Required if DVTSourceControlWorkspaceBlueprintLocationTypeKey is DVTSourceControlPathLocation:`
19. `DVTSourceControlPathIdentifierKey: string (relative path in repository)`
20. `*/`
21. `"DVTSourceControlWorkspaceBlueprintLocationsKey": {`
22. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": {`
23. `"DVTSourceControlBranchIdentifierKey": "trunk",`
24. `"DVTSourceControlBranchOptionsKey": 5,`
25. `"DVTSourceControlWorkspaceBlueprintLocationTypeKey": "DVTSourceControlBranch"`
26. `}`
27. `},`
28. `/* Working Copy Repository Locations`
29. `Value: dictionary of string (repository identifier) to <Branch and Tag Locations>`
30. `Branch and Tag Locations:`
31. `DVTSourceControlWorkingCopyRepositoryBranchesLocationKey: string (relative path in repository to branches folder)`
32. `DVTSourceControlWorkingCopyRepositoryTagsLocationKey: string (relative path in repository to tags folder)`
33. `DVTSourceControlWorkingCopyRepositoryPrimaryBranchLocationKey: string (relative path in repository to trunk folder)`
34. `*/`
35. `"DVTSourceControlWorkspaceBlueprintWorkingCopyRepositoryLocationsKey" : {`
36. `"34768997-536d-3cd6-3966-ce57b7db7bff" : {`
37. `"DVTSourceControlWorkingCopyRepositoryBranchesLocationKey" : "branches",`
38. `"DVTSourceControlWorkingCopyRepositoryTagsLocationKey" : "tags",`
39. `"DVTSourceControlWorkingCopyRepositoryPrimaryBranchLocationKey" : "trunk"`
40. `}`
41. `},`
42. `/* The name for the blueprint, typically the name of the Xcode project or workspace`
43. `Value: string`
44. `*/`
45. `"DVTSourceControlWorkspaceBlueprintNameKey": "Project",`
46. `/* The identifier of the working copy containing the Xcode project or workspace to build, considered the primary working copy`
47. `Value: string (repository identifier)`
48. `*/`
49. `"DVTSourceControlWorkspaceBlueprintPrimaryRemoteRepositoryKey": "360BCE85-D2C0-4DE1-937B-4A56E07173E6",`
50. `/* The relative path in the primary working copy to the Xcode project or workspace to build`
51. `Value: string (relative path)`
52. `*/`
53. `"DVTSourceControlWorkspaceBlueprintRelativePathToProjectKey": "Project.xcworkspace",`
54. `/* Repositories`
55. `Value: array of <Repository>`
56. `Repository:`
57. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey: true (requied)`
58. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey: string (consistent identifier within blueprint, SVN UUID)`
59. `DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey: "com.apple.dt.Xcode.sourcecontrol.Subversion" (Subversion)`
60. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey: a string of one of the following fingerprint options:`
61. `RSA (SSH servers) |`
62. `MD5 (self-signed SSL server certificates)`
63. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey: string (URI)`
64. `*/`
65. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoriesKey": [`
66. `{`
67. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryEnforceTrustCertFingerprintKey": true,`
68. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryIdentifierKey": "360BCE85-D2C0-4DE1-937B-4A56E07173E6",`
69. `"DVTSourceControlWorkspaceBlueprintRemoteRepositorySystemKey": "com.apple.dt.Xcode.sourcecontrol.Subversion",`
70. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryTrustedCertFingerprintKey": "174F678B9ED220D9C8B2A47F42392A44",`
71. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryURLKey": "svn+ssh:\/\/server.example.com\/svn\/repo"`
72. `}`
73. `],`
74. `/* Authentication Strategies`
75. `Value: dictionary of string (repository identifier) to <Authentication>`
76. `Authentication:`
77. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey:`
78. `"DVTSourceControlAuthenticationStrategy" (Anonymous) |`
79. `"DVTSourceControlBasicAuthenticationStrategy" (Username and Password) |`
80. `"DVTSourceControlSSHKeysAuthenticationStrategy" (SSH Keys)`
81. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey: string (Password or Passphrase)`
82. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey: string (Username)`
83. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPublicKeyDataKey: string (Base64-encoded public key data)`
84. `DVTSourceControlWorkspaceBlueprintRemoteRepositoryPrivateKeyDataKey: string (Base64-encoded private key data)`
85. `*/`
86. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationStrategiesKey": {`
87. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": {`
88. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryAuthenticationTypeKey": "DVTSourceControlBasicAuthenticationStrategy",`
89. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryPasswordKey": "password",`
90. `"DVTSourceControlWorkspaceBlueprintRemoteRepositoryUsernameKey": "me"`
91. `}`
92. `},`
93. `/* The blueprint format version`
94. `Value: 204`
95. `*/`
96. `"DVTSourceControlWorkspaceBlueprintVersion": 204,`
97. `/* Working Copy Layout`
98. `Value: dictionary of string (repository identifier) to string (relative path of checkout)`
99. `*/`
100. `"DVTSourceControlWorkspaceBlueprintWorkingCopyPathsKey": {`
101. `"360BCE85-D2C0-4DE1-937B-4A56E07173E6": "Project/"`
102. `},`
103. `}`

[Schema](Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqnrnknltc)

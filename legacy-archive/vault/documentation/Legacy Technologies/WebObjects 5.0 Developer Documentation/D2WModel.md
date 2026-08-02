---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WModel.html
archived_at: '2026-07-15T08:12:44.245119Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WModel__

__Package__:
com.webobjects.directtoweb

__Inherits from__:java.lang.Object__Subclasses__:

- [D2WFastModel](D2WFastModel.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [protected D2WModel(EOKeyValueUnarchiver unarchiver)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxuimsxjvxwizlmf5cdev2nn5sgk3bpfbcu6s3fpflgc3dvmvkw4ylsmnugs5tfoiuq)
- [protected D2WModel(File file)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxuimsxjvxwizlmf5cdev2nn5sgk3bpfbdgs3dffe)
- [protected D2WModel(NSArray anArray)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxuimsxjvxwizlmf5cdev2nn5sgk3bpfbhfgqlsojqxski)

---

Static Constants

- [actionsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bmn2gs33oonfwk6i)
- [allMarker](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bnrwe2ylsnnsxe)
- [allowCollapsingKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bnrwg652dn5wgyylqonuw4z2lmv4q)
- [alternateRowColorKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bnr2gk4tomf2gkutpo5bw63dpojfwk6i)
- [attributeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bor2he2lcov2gks3fpe)
- [attributeTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3bor2he2lcov2gkvdzobsuwzlz)
- [backgroundColorForPageKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3cmfrwwz3sn52w4zcdn5wg64sgn5zfaylhmvfwk6i)
- [backgroundColorForTableKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3cmfrwwz3sn52w4zcdn5wg64sgn5zfiylcnrsuwzlz)
- [batchKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3cmf2gg2clmv4q)
- [boldKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3cn5wgis3fpe)
- [borderKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3cn5zgizlsjnsxs)
- [colorKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dn5wg64slmv4q)
- [componentAvailableKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dn5wxa33omvxhiqlwmfuwyylcnrsuwzlz)
- [componentBorderKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dn5wxa33omvxhiqtpojsgk4slmv4q)
- [componentNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dn5wxa33omvxhittbnvsuwzlz)
- [componentsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dn5wxa33omvxhi42lmv4q)
- [customTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3dovzxi33nkr4xazklmv4q)
- [displayNameForPropertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3enfzxa3dbpfhgc3lfizxxeudsn5ygk4tupffwk6i)
- [displayPropertyKeysKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3enfzxa3dbpfihe33qmvzhi6klmv4xgs3fpe)
- [dummyTrue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3eovww26kuoj2wk)
- [dummyTrueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3eovww26kuoj2wks3fpe)
- [dynamicPageKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3epfxgc3ljmnigcz3fjnsxs)
- [editIconKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3fmruxisldn5xewzlz)
- [editorsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3fmruxi33sonfwk6i)
- [entitiesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3fnz2gs5djmvzuwzlz)
- [entityKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3fnz2gs5dzjnsxs)
- [formatterKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3gn5zg2yluorsxes3fpe)
- [frameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3gojqw2zklmv4q)
- [framesActiveKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3gojqw2zltifrxi2lwmvfwk6i)
- [headerNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3imvqwizlsjzqw2zklmv4q)
- [inspectComponentNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3jnzzxazldorbw63lqn5xgk3tujzqw2zklmv4q)
- [inspectIconKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3jnzzxazldorewg33ojnsxs)
- [isGeneratingKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3jondwk3tfojqxi2lom5fwk6i)
- [italicKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3jorqwy2ldjnsxs)
- [justificationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3kovzxi2lgnfrwc5djn5xewzlz)
- [keyPathTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3lmv4vaylunbkhs4dfjnsxs)
- [keyWhenRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3lmv4vo2dfnzjgk3dboruw63ttnbuxas3fpe)
- [lengthKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3mmvxgo5dijnsxs)
- [lookKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3mn5xwws3fpe)
- [noneMarker](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3on5xgktlbojvwk4q)
- [numColsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3oovwug33monfwk6i)
- [one](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3pnzsq)
- [pageAvailableKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qmftwkqlwmfuwyylcnrsuwzlz)
- [pageNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qmftwkttbnvsuwzlz)
- [pageWrapperNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qmftwkv3smfyhazlsjzqw2zklmv4q)
- [passwordKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qmfzxg53pojsewzlz)
- [propertyIsKeyPathKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qojxxazlsor4us42lmv4vaylunbfwk6i)
- [propertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qojxxazlsor4uwzlz)
- [propertyKeyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qojxxazlsor4uwzlzjnsxs)
- [propertyKeyPortionInModelKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qojxxazlsor4uwzlzkbxxe5djn5xes3snn5sgk3clmv4q)
- [propertyTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3qojxxazlsor4vi6lqmvfwk6i)
- [readOnlyEntityNamesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3smvqwit3onr4uk3tunf2hsttbnvsxgs3fpe)
- [relationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3smvwgc5djn5xhg2djobfwk6i)
- [relationshipTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3smvwgc5djn5xhg2djobkhs4dfjnsxs)
- [rulesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3sovwgk42lmv4q)
- [sessionKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3tmvzxg2lpnzfwk6i)
- [showBannerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3tnbxxoqtbnzxgk4slmv4q)
- [startupEntityNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3torqxe5dvobcw45djor4u4ylnmvfwk6i)
- [startupTaskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3torqxe5dvobkgc43ljnsxs)
- [subTaskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3tovrfiyltnnfwk6i)
- [superTaskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3tovygk4sumfzwws3fpe)
- [supportsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3tovyha33sorzuwzlz)
- [targetKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3umfzgozlujnsxs)
- [taskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3umfzwws3fpe)
- [thresholdKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3unbzgk43in5wgis3fpe)
- [uiStyleKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3vnfjxi6lmmvfwk6i)
- [userNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3vonsxettbnvsuwzlz)
- [visibleEntityNamesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3wnfzwsytmmvcw45djor4u4ylnmvzuwzlz)
- [webAssistantPageNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl3xmvrec43tnfzxiyloorigcz3fjzqw2zklmv4q)
- [zero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlpmrswyl32mvzg6)

---

- [userClientConfigurationFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxk43fojbwy2lfnz2eg33omzuwo5lsmf2gs33oizuwyzjpizuwyzjpfauq)

Private Methods

- [addRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwczdekj2wyzjpozxwszbpfbjhk3dffe)
- [addRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwczdekj2wyzltf53g62lef4ue4u2bojzgc6jj)
- [addRuleToItsBucket](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwczdekj2wyzkun5exi42covrwwzluf53g62lef4ufe5lmmuuq)
- [addRuleTrace](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwczdekj2wyzkuojqwgzjpozxwszbpfbjhk3dffe)
- [candidates](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwgylomruwiylumvzs6vtfmn2g64rpfbjxi4tjnztsyrbsk5bw63tumv4hiki)
- [canSaveUserModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwgyloknqxmzkvonsxetlpmrswyl3cn5xwyzlbnyxsqki)
- [checkPossibilityToSaveUserModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg2dfmnvva33tonuwe2lmnf2hsvdpknqxmzkvonsxetlpmrswyl3cn5xwyzlbnyxsqytpn5wgkylofe)
- [checkRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg2dfmnvve5lmmvzs65tpnfsc6kbj)
- [clientConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg3djmvxhiq3pnztgsz3vojqxi2lpnyxuqyltnb2gcytmmuxsqki)
- [clientConfigurationFilesInBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg3djmvxhiq3pnztgsz3vojqxi2lpnzdgs3dfonew4qtvnzsgyzltf5lgky3un5zc6kbj)
- [componentDefinitions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg33nobxw4zloorcgkztjnzuxi2lpnzzs6sdbonuhiylcnrss6kbj)
- [createWebAssistantRulesWithSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwg4tfmf2gkv3fmjaxg43jon2gc3tukj2wyzltk5uxi2ctmv2hi2lom5zs65tpnfsc6kctmvzhmzlsknuwizktmv2hi2lom5zss)
- [dataTypesInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwiylumfkhs4dfonew45tpnr3gkzbpkzswg5dpoixsqki)
- [defaultModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2nn5sgk3bpmrswmylvnr2e233emvwc6rbsk5gw6zdfnqxsqki)
- [dirty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwi2lsor4s6ytpn5wgkylof4ucs)
- [dynamicPages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwi6lomfwwsy2qmftwk4zpkzswg5dpoixsqki)
- [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwkzdjorxxe4zpjbqxg2dumfrgyzjpfauq)
- [encodeWebAssistantRulesWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwk3tdn5sgkv3fmjaxg43jon2gc3tukj2wyzltk5uxi2clmv4vmylmovsuc4tdnbuxmzlsf5hfgrdjmn2gs33omfzhslziivhuwzlzkzqwy5lfifzgg2djozsxeki)
- [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwk3tdn5sgkv3joruewzlzkzqwy5lfifzgg2djozsxel2okncgsy3unfxw4ylspexsqrkpjnsxsvtbnr2wkqlsmnugs5tfoiuq)
- [fireAllRulesForKeyPathInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwm2lsmvawy3csovwgk42gn5zewzlzkbqxi2cjnzbw63tumv4hil2wmvrxi33sf4ufg5dsnfxgolcegjlug33oorsxq5bj)
- [fireRuleForKeyPathInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwm2lsmvjhk3dfizxxes3fpfigc5dijfxeg33oorsxq5bpj5rguzldoqxsqu3uojuw4zzmiqzfoq3pnz2gk6dufe)
- [fireSystemRuleForKeyPathInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwm2lsmvjxs43umvwve5lmmvdg64slmv4vaylunbew4q3pnz2gk6duf5hwe2tfmn2c6kctorzgs3thfrcdev2dn5xhizlyoquq)
- [inferrableKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxws3tgmvzheylcnrsuwzlzomxuqyltnb2gcytmmuxsqki)
- [initializeClientConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxws3tjoruwc3djpjsug3djmvxhiq3pnztgsz3vojqxi2lpnyxxm33jmqxsqki)
- [invalidateCaches](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxws3twmfwgszdborsugyldnbsxgl3wn5uwilzife)
- [isPageStatic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxws42qmftwku3umf2gsyzpmjxw63dfmfxc6kctorzgs3thfrcdev2dn5xhizlyoquq)
- [loadRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxwy33bmrjhk3dfomxxm33jmqxsqki)
- [mergeFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxw2zlsm5sum2lmmuxxm33jmqxsqrtjnrsss)
- [modelFilesInBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxw233emvwem2lmmvzus3scovxgi3dfomxvmzldorxxelzife)
- [nameFromFrameworkBundle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2nn5sgk3bpnzqw2zkgojxw2rtsmfwwk53pojvue5lomrwgkl2torzgs3thf4ue4u2covxgi3dffe)
- [newSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxw4zlxknsxi5djnztxgl3wn5uwilziknsxe5tfojjwszdfknsxi5djnztxgki)
- [pageRuleKeysForPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxaylhmvjhk3dfjnsxs42gn5zfaylhmuxvmzldorxxelzikn2he2lom4uq)
- [pageRuleKeysFromClientConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxaylhmvjhk3dfjnsxs42gojxw2q3mnfsw45cdn5xgm2lhovzgc5djn5xc6vtfmn2g64rpfauq)
- [propertyRuleKeysForComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxa4tpobsxe5dzkj2wyzklmv4xgrtpojbw63lqn5xgk3tuomxvmzldorxxelzikzswg5dpoiuq)
- [propertyRuleKeysFromClientConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxa4tpobsxe5dzkj2wyzklmv4xgrtsn5wug3djmvxhiq3pnztgsz3vojqxi2lpnyxvmzldorxxelzife)
- [removeAllWebAssistantRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxezlnn53gkqlmnrlwkysbonzws43umfxhiutvnrsxgl3wn5uwilzife)
- [removeDynamicPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxezlnn53gkrdznzqw22ldkbqwozjpozxwszbpfbjwk4twmvzfg2lemvjwk5dunfxgo4zj)
- [removeRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxezlnn53gkutvnrss65tpnfsc6kcsovwgkki)
- [removeWebAssistantRulesWithSameContextAsSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxezlnn53gkv3fmjaxg43jon2gc3tukj2wyzltk5uxi2ctmfwwkq3pnz2gk6duifzvgzluoruw4z3tf53g62lef4ufgzluoruw4z3tfe)
- [revertWebAssistantRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxezlwmvzhiv3fmjaxg43jon2gc3tukj2wyzltf53g62lef4ucs)
- [saveWebAssistantRulesIntoUsedModelFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxgylwmvlwkysbonzws43umfxhiutvnrsxgsloorxvk43fmrgw6zdfnrdgs3dff53g62lef4ucs)
- [setDefaultModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2nn5sgk3bponsxirdfmzqxk3dujvxwizlmf53g62lef4ueimsxjvxwizlmfe)
- [setDirty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxgzluiruxe5dzf53g62lef4uge33pnrswc3rj)
- [setRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxgzlukj2wyzltf53g62lef4ue4u2bojzgc6jj)
- [sortRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxg33sorjhk3dfomxxm33jmqxsqki)
- [tasks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxiyltnnzs6rloovwwk4tboruw63rpfauq)
- [taskVector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxiyltnnlgky3un5zc6vtfmn2g64rpfauq)
- [toFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxi32gnfwgkl3wn5uwilziizuwyzjj)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxi32torzgs3thf5jxi4tjnzts6kbj)
- [typeForRuleKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxi6lqmvdg64ssovwgks3fpexvg5dsnfxgolzikn2he2lom4uq)
- [updateUserSettingsForNewPageAvailableRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxk4demf2gkvltmvzfgzluoruw4z3tizxxettfo5igcz3fif3gc2lmmfrgyzksovwgkl3wn5uwilziknsxe5tfojjwszdfknsxi5djnztxglctorzgs3thfe)
- [userModelFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxk43fojgw6zdfnrdgs3dff5dgs3dff4ucs)
- [webAssistantRulesForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gw6zdfnqxxozlcifzxg2ltorqw45csovwgk42gn5zfgylwmuxu4u2bojzgc6jpfauq)

---

__Constructors__

---

__D2WModel__

protected D2WModel(EOKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__D2WModel__

protected D2WModel(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__D2WModel__

protected D2WModel(NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__actionsKey__
java.lang.String

This constant is intentionally undocumented.

---

__allMarker__
java.lang.String

This constant is intentionally undocumented.

---

__allowCollapsingKey__
java.lang.String

This constant is intentionally undocumented.

---

__alternateRowColorKey__
java.lang.String

This constant is intentionally undocumented.

---

__attributeKey__
java.lang.String

This constant is intentionally undocumented.

---

__attributeTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__backgroundColorForPageKey__
java.lang.String

This constant is intentionally undocumented.

---

__backgroundColorForTableKey__
java.lang.String

This constant is intentionally undocumented.

---

__batchKey__
java.lang.String

This constant is intentionally undocumented.

---

__boldKey__
java.lang.String

This constant is intentionally undocumented.

---

__borderKey__
java.lang.String

This constant is intentionally undocumented.

---

__colorKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentAvailableKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentBorderKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentsKey__
java.lang.String

This constant is intentionally undocumented.

---

__customTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__displayNameForPropertyKey__
java.lang.String

This constant is intentionally undocumented.

---

__displayPropertyKeysKey__
java.lang.String

This constant is intentionally undocumented.

---

__dummyTrue__
java.lang.String

This constant is intentionally undocumented.

---

__dummyTrueKey__
java.lang.String

This constant is intentionally undocumented.

---

__dynamicPageKey__
java.lang.String

This constant is intentionally undocumented.

---

__editIconKey__
java.lang.String

This constant is intentionally undocumented.

---

__editorsKey__
java.lang.String

This constant is intentionally undocumented.

---

__entitiesKey__
java.lang.String

This constant is intentionally undocumented.

---

__entityKey__
java.lang.String

This constant is intentionally undocumented.

---

__formatterKey__
java.lang.String

This constant is intentionally undocumented.

---

__frameKey__
java.lang.String

This constant is intentionally undocumented.

---

__framesActiveKey__
java.lang.String

This constant is intentionally undocumented.

---

__headerNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__inspectComponentNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__inspectIconKey__
java.lang.String

This constant is intentionally undocumented.

---

__isGeneratingKey__
java.lang.String

This constant is intentionally undocumented.

---

__italicKey__
java.lang.String

This constant is intentionally undocumented.

---

__justificationKey__
java.lang.String

This constant is intentionally undocumented.

---

__keyPathTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__keyWhenRelationshipKey__
java.lang.String

This constant is intentionally undocumented.

---

__lengthKey__
java.lang.String

This constant is intentionally undocumented.

---

__lookKey__
java.lang.String

This constant is intentionally undocumented.

---

__noneMarker__
java.lang.String

This constant is intentionally undocumented.

---

__numColsKey__
java.lang.String

This constant is intentionally undocumented.

---

__one__
java.lang.Integer

This constant is intentionally undocumented.

---

__pageAvailableKey__
java.lang.String

This constant is intentionally undocumented.

---

__pageNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__pageWrapperNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__passwordKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyIsKeyPathKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyKeyKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyKeyPortionInModelKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__readOnlyEntityNamesKey__
java.lang.String

This constant is intentionally undocumented.

---

__relationshipKey__
java.lang.String

This constant is intentionally undocumented.

---

__relationshipTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__rulesKey__
java.lang.String

This constant is intentionally undocumented.

---

__sessionKey__
java.lang.String

This constant is intentionally undocumented.

---

__showBannerKey__
java.lang.String

This constant is intentionally undocumented.

---

__startupEntityNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__startupTaskKey__
java.lang.String

This constant is intentionally undocumented.

---

__subTaskKey__
java.lang.String

This constant is intentionally undocumented.

---

__superTaskKey__
java.lang.String

This constant is intentionally undocumented.

---

__supportsKey__
java.lang.String

This constant is intentionally undocumented.

---

__targetKey__
java.lang.String

This constant is intentionally undocumented.

---

__taskKey__
java.lang.String

This constant is intentionally undocumented.

---

__thresholdKey__
java.lang.String

This constant is intentionally undocumented.

---

__uiStyleKey__
java.lang.String

This constant is intentionally undocumented.

---

__userNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__visibleEntityNamesKey__
java.lang.String

This constant is intentionally undocumented.

---

__webAssistantPageNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__zero__
java.lang.Integer

This constant is intentionally undocumented.

---

__Methods__

__addRule__

protected void addRule(Rule aRule)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__addRules__

protected void addRules(NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__addRuleToItsBucket__

protected void addRuleToItsBucket(Rule aRule)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__addRuleTrace__

protected void addRuleTrace(Rule aRule)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__candidates__

protected Vector candidates(String aString, D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__canSaveUserModel__

public boolean canSaveUserModel()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__checkPossibilityToSaveUserModel__

public boolean checkPossibilityToSaveUserModel(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__checkRules__

public void checkRules()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__clientConfiguration__

public Hashtable clientConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__clientConfigurationFilesInBundles__

public Vector clientConfigurationFilesInBundles()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentDefinitions__

public Hashtable componentDefinitions()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__createWebAssistantRulesWithSettings__

protected void createWebAssistantRulesWithSettings(ServerSideSettings settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dataTypesInvolved__

protected Vector dataTypesInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__defaultModel__

public static D2WModel defaultModel()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dirty__

public boolean dirty()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dynamicPages__

protected Vector dynamicPages()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__editors__

public Hashtable editors()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__encodeWebAssistantRulesWithKeyValueArchiver__

protected NSDictionary encodeWebAssistantRulesWithKeyValueArchiver(EOKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__encodeWithKeyValueArchiver__

protected NSDictionary encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__fireAllRulesForKeyPathInContext__

protected Vector fireAllRulesForKeyPathInContext(String aString, D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__fireRuleForKeyPathInContext__

protected Object fireRuleForKeyPathInContext(String aString, D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__fireSystemRuleForKeyPathInContext__

protected Object fireSystemRuleForKeyPathInContext(String aString, D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inferrableKeys__

public Hashtable inferrableKeys()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__initializeClientConfiguration__

protected void initializeClientConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__invalidateCaches__

protected void invalidateCaches()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isPageStatic__

public boolean isPageStatic(String aString, D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__loadRules__

public void loadRules()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__mergeFile__

protected void mergeFile(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__modelFilesInBundles__

public Vector modelFilesInBundles()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__nameFromFrameworkBundle__

static public String nameFromFrameworkBundle(NSBundle bundle)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__newSettings__

protected void newSettings(ServerSideSettings settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__pageRuleKeysForPage__

public Vector pageRuleKeysForPage(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__pageRuleKeysFromClientConfiguration__

public Vector pageRuleKeysFromClientConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyRuleKeysForComponents__

public Vector propertyRuleKeysForComponents(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyRuleKeysFromClientConfiguration__

public Vector propertyRuleKeysFromClientConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__removeAllWebAssistantRules__

protected void removeAllWebAssistantRules()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__removeDynamicPage__

protected void removeDynamicPage(ServerSideSettings settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__removeRule__

protected void removeRule(Rule aRule)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__removeWebAssistantRulesWithSameContextAsSettings__

protected void removeWebAssistantRulesWithSameContextAsSettings(Settings settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__revertWebAssistantRules__

protected void revertWebAssistantRules()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__saveWebAssistantRulesIntoUsedModelFile__

protected void saveWebAssistantRulesIntoUsedModelFile()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDefaultModel__

static public void setDefaultModel(D2WModel aModel)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDirty__

protected void setDirty(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setRules__

protected void setRules(NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__sortRules__

protected void sortRules()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__tasks__

protected Enumeration tasks()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__taskVector__

protected Vector taskVector()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toFile__

protected void toFile(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toString__

public String toString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__typeForRuleKey__

public final String typeForRuleKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__updateUserSettingsForNewPageAvailableRule__

public void updateUserSettingsForNewPageAvailableRule(ServerSideSettings settings, String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__userClientConfigurationFile__

public File userClientConfigurationFile()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__userModelFile__

public File userModelFile()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__webAssistantRulesForSave__

protected NSArray webAssistantRulesForSave()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

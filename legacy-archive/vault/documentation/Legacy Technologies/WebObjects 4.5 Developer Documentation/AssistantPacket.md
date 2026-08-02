---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/AssistantPacket.html
archived_at: '2026-07-15T08:11:28.313575Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__AssistantPacket__

__Package__:
com.apple.client.directtoweb.common

__Inherits from__:java.lang.Object__Implements__:

- [D2WKeyValueArchiving](D2WKeyValueArchiving.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public AssistantPacket()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuxg5dbnz2fayldnnsxil2bonzws43umfxhiudbmnvwk5bpifzxg2ltorqw45cqmfrwwzluf4ucs)

---

Static Constants

- [actionKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5qwg5djn5xewzlz)
- [assistantPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5qxg43jon2gc3tukbxxe5a)
- [clientConfigurationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5rwy2lfnz2eg33omzuwo5lsmf2gs33ojnsxs)
- [deleteDynamicPageId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5sgk3dforsui6lomfwwsy2qmftwksle)
- [errorId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5sxe4tpojewi)
- [errorKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5sxe4tpojfwk6i)
- [generateDynamicTemplateId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk3tfojqxizkepfxgc3ljmnkgk3lqnrqxizkjmq)
- [generateId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk3tfojqxizkjmq)
- [getChildrenForPropertyActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk5cdnbuwyzdsmvxem33skbzg64dfoj2hsqldoruw63sjmq)
- [getClientConfigurationId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk5cdnruwk3tuinxw4ztjm52xeylunfxw4sle)
- [getPropertyActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk5cqojxxazlsor4ucy3unfxw4sle)
- [getSettingsActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5twk5ctmv2hi2lom5zucy3unfxw4sle)
- [newSettingsActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5xgk52tmv2hi2lom5zucy3unfxw4sle)
- [okId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5xwwsle)
- [packetIDKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5ygcy3lmv2esrclmv4q)
- [propertyChildrenKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5yhe33qmvzhi6kdnbuwyzdsmvxewzlz)
- [propertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5yhe33qmvzhi6klmv4q)
- [refreshId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zgkztsmvzwqsle)
- [refreshTargetId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zgkztsmvzwqvdbojtwk5cjmq)
- [removeCustomSettingsActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zgk3lpozsug5ltorxw2u3for2gs3thonawg5djn5xesza)
- [revertSettingsActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zgk5tfoj2fgzluoruw4z3tifrxi2lpnzewi)
- [saveSettingsActionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwc5tfknsxi5djnztxgqldoruw63sjmq)
- [sessionIdKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwk43tnfxw4slejnsxs)
- [settingsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwk5dunfxgo42lmv4q)
- [showAssistantId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwq33xifzxg2ltorqw45cjmq)
- [urlKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf52xe3clmv4q)

---

Fields

- [action](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5qwg5djn5xa)
- [clientConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5rwy2lfnz2eg33omzuwo5lsmf2gs33o)
- [error](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5sxe4tpoi)
- [packetID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5ygcy3lmv2esra)
- [property](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5yhe33qmvzhi6i)
- [propertyChildren](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5yhe33qmvzhi6kdnbuwyzdsmvxa)
- [sessionId](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwk43tnfxw4sle)
- [settings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf5zwk5dunfxgo4y)
- [url](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2ltorqw45cqmfrwwzluf52xe3a)

---

Private Methods

- [decodeWithD2WKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuxg5dbnz2fayldnnsxil3emvrw6zdfk5uxi2cegjluwzlzkzqwy5lfkvxgc4tdnbuxmzlsf53g62lef4ueimsxjnsxsvtbnr2wkvlomfzgg2djozsxeki)
- [encodeWithD2WKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuxg5dbnz2fayldnnsxil3fnzrw6zdfk5uxi2cegjluwzlzkzqwy5lfifzgg2djozsxel3wn5uwilziiqzfos3fpflgc3dvmvaxey3inf3gk4rj)
- [newPacketID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5axg43jon2gc3tukbqwg23foqxw4zlxkbqwg23foreuil3jnz2c6kbj)
- [readFromInputStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5axg43jon2gc3tukbqwg23foqxxezlbmrdhe33njfxha5lukn2hezlbnuxuc43tnfzxiyloorigcy3lmv2c6kcemf2gcsloob2xiu3uojswc3jmiqzfos3fpflgc3dvmvaxey3inf3gs3thirswyzlhmf2gkki)
- [sendToOutputStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuxg5dbnz2fayldnnsxil3tmvxgivdpj52xi4dvorjxi4tfmfws65tpnfsc6kcemf2gct3voryhk5ctorzgkylnfrcdev2lmv4vmylmovsuc4tdnbuxm2lom5cgk3dfm5qxizjj)

---

__Constructors__

---

__com.apple.client.directtoweb.common.AssistantPacket__

public AssistantPacket()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__actionKey__
java.lang.String

This constant is intentionally undocumented.

---

__assistantPort__
int

This constant is intentionally undocumented.

---

__clientConfigurationKey__
java.lang.String

This constant is intentionally undocumented.

---

__deleteDynamicPageId__
java.lang.String

This constant is intentionally undocumented.

---

__errorId__
java.lang.String

This constant is intentionally undocumented.

---

__errorKey__
java.lang.String

This constant is intentionally undocumented.

---

__generateDynamicTemplateId__
java.lang.String

This constant is intentionally undocumented.

---

__generateId__
java.lang.String

This constant is intentionally undocumented.

---

__getChildrenForPropertyActionId__
java.lang.String

This constant is intentionally undocumented.

---

__getClientConfigurationId__
java.lang.String

This constant is intentionally undocumented.

---

__getPropertyActionId__
java.lang.String

This constant is intentionally undocumented.

---

__getSettingsActionId__
java.lang.String

This constant is intentionally undocumented.

---

__newSettingsActionId__
java.lang.String

This constant is intentionally undocumented.

---

__okId__
java.lang.String

This constant is intentionally undocumented.

---

__packetIDKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyChildrenKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertyKey__
java.lang.String

This constant is intentionally undocumented.

---

__refreshId__
java.lang.String

This constant is intentionally undocumented.

---

__refreshTargetId__
java.lang.String

This constant is intentionally undocumented.

---

__removeCustomSettingsActionId__
java.lang.String

This constant is intentionally undocumented.

---

__revertSettingsActionId__
java.lang.String

This constant is intentionally undocumented.

---

__saveSettingsActionId__
java.lang.String

This constant is intentionally undocumented.

---

__sessionIdKey__
java.lang.String

This constant is intentionally undocumented.

---

__settingsKey__
java.lang.String

This constant is intentionally undocumented.

---

__showAssistantId__
java.lang.String

This constant is intentionally undocumented.

---

__urlKey__
java.lang.String

This constant is intentionally undocumented.

---

__Fields__

---

__action__
java.lang.String

This constant is intentionally undocumented.

---

__clientConfiguration__
java.lang.Object

This constant is intentionally undocumented.

---

__error__
java.lang.String

This constant is intentionally undocumented.

---

__packetID__
int

This constant is intentionally undocumented.

---

__property__
com.apple.client.directtoweb.common.Property

This constant is intentionally undocumented.

---

__propertyChildren__
java.util.Vector

This constant is intentionally undocumented.

---

__sessionId__
java.lang.String

This constant is intentionally undocumented.

---

__settings__
com.apple.client.directtoweb.common.Settings

This constant is intentionally undocumented.

---

__url__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__decodeWithD2WKeyValueUnarchiver__

public void decodeWithD2WKeyValueUnarchiver(D2WKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__encodeWithD2WKeyValueArchiver__

public void encodeWithD2WKeyValueArchiver(D2WKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__newPacketID__

public static int newPacketID()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__readFromInputStream__

public static AssistantPacket readFromInputStream(DataInputStream stream, D2WKeyValueArchivingDelegate delegate)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__sendToOutputStream__

public void sendToOutputStream(DataOutputStream stream, D2WKeyValueArchivingDelegate delegate)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

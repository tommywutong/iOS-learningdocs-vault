---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WContext.html
archived_at: '2026-07-15T08:11:28.610317Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WContext__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:java.lang.Object__Implements__:

- com.apple.yellow.foundation.NSKeyValueCoding

---

__Class Description__

---

Direct to Web contexts are objects of the D2WContext class. When a Direct to Web template renders, it does so with the help of a Direct to Web context which provides values for bindings in the template and maintains state information about the rendering process. See the "Direct to Web Architecture" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about the Direct to Web context.

The primary function of the Direct to Web context is to implement the EOKeyValueCoding interface (defined in the EOControl framework) by implementing `valueForKey` and `takeValueForKey`. It resolves the keys with the help of the rule system. D2WContext also provides two methods for accessing key paths such as `entity.name`. These are `valueForKeyPath` and `takeValueForKeyPath`. When you use the `d2wContext` key in a Direct to Web template's bindings (`.wod`) file, you indirectly use one of these methods.

For a list of the keys implemented by the D2WContext, see [Direct To Web Context Keys](Direct%20to%20Web%20Context%20Keys.md).

The D2WContext class also provides convenience methods to access keys in Java.

__Method Types__

---

Constructors

- [public D2WContext()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil2egjlug33oorsxq5bpiqzfoq3pnz2gk6duf4ucs)
- [public D2WContext(D2WContext d2wContext)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil2egjlug33oorsxq5bpiqzfoq3pnz2gk6duf4ueimsxinxw45dfpb2cs)
- [D2WContext(Settings settings)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil2egjlug33oorsxq5bpiqzfoq3pnz2gk6duf4ufgzluoruw4z3tfe)
- [public D2WContext(WOSession session)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil2egjlug33oorsxq5bpiqzfoq3pnz2gk6duf4ufot2tmvzxg2lpnyuq)

---

Static Constants

- [NULL_VALUE](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoq3pnz2gk6duf5hfktcml5lectcviu)
- [VALUE_TO_BE_DERIVED](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoq3pnz2gk6duf5lectcvivpvit27ijcv6rcfkjevmrke)

---

Convenience Methods

- [attribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3bor2he2lcov2gkl2fj5axi5dsnfrhk5dff4ucs)
- [componentName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3dn5wxa33omvxhittbnvss6u3uojuw4zzpfauq)
- [displayNameForProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3enfzxa3dbpfhgc3lfizxxeudsn5ygk4tupexvg5dsnfxgolzife)
- [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3fnz2gs5dzf5cu6rlooruxi6jpfauq)
- [pageName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3qmftwkttbnvss6u3uojuw4zzpfauq)
- [propertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3qojxxazlsor4uwzlzf5jxi4tjnzts6kbj)
- [propertyType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3qojxxazlsor4vi6lqmuxws3tuf4ucs)
- [relationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3smvwgc5djn5xhg2djoaxukt2smvwgc5djn5xhg2djoaxsqki)
- [setPropertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3tmv2fa4tpobsxe5dzjnsxsl3wn5uwilzikn2he2lom4uq)
- [startupEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3torqxe5dvobcw45djor4u4ylnmuxvg5dsnfxgolzife)
- [startupTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3torqxe5dvobkgc43lf5jxi4tjnzts6kbj)
- [task](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3umfzwwl2torzgs3thf4ucs)

Key-Value Coding

- [keyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3lmv4vo2dfnzjgk3dboruw63ttnbuxal2torzgs3thf4ucs)

Private Methods

- [attribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3bor2he2lcov2gkl2fj5axi5dsnfrhk5dff4ufg5dsnfxgoki)
- [clearDerivedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3dnrswc4semvzgs5tfmrlgc3dvmvzs65tpnfsc6kbj)
- [componentClassPresentInRuntime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3dn5wxa33omvxhiq3mmfzxgudsmvzwk3tujfxfe5looruw2zjpmjxw63dfmfxc6kctorzgs3thfe)
- [componentsAvailable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3dn5wxa33omvxhi42bozqws3dbmjwgkl2wmvrxi33sf4ucs)
- [computeDerivedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3dn5wxa5lumvcgk4tjozswivtbnr2wk4zpozxwszbpfauq)
- [distantAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3enfzxiylooraxi5dsnfrhk5dff5cu6qluorzgsytvorss6kctorzgs3thfrcu6rlooruxi6jj)
- [distantRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3enfzxiyloorjgk3dboruw63ttnbuxal2fj5jgk3dboruw63ttnbuxalzikn2he2lom4wekt2fnz2gs5dzfe)
- [dynamicPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3epfxgc3ljmnigcz3ff5jxi4tjnzts6kbj)
- [frame](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3gojqw2zjpmjxw63dfmfxc6kbj)
- [inferAllPossibleValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3jnztgk4sbnrwfa33tonuwe3dfkzqwy5lfondg64slmv4s6vtfmn2g64rpfbjxi4tjnztss)
- [inferSystemValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3jnztgk4stpfzxizlnkzqwy5lfizxxes3fpexu6ytkmvrxilzikn2he2lom4uq)
- [inferValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3jnztgk4swmfwhkzkgn5zewzlzf5hwe2tfmn2c6kctorzgs3thfe)
- [isGenerating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3jondwk3tfojqxi2lom4xwe33pnrswc3rpfauq)
- [model](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3nn5sgk3bpiqzfotlpmrswylzife)
- [nullOutDerivedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3oovwgyt3vorcgk4tjozswivtbnr2wk4zpozxwszbpfauq)
- [pagesAvailable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3qmftwk42bozqws3dbmjwgkl2wmvrxi33sf4ucs)
- [propertyKeyIsKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3qojxxazlsor4uwzlzjfzuwzlzkbqxi2bpmjxw63dfmfxc6kbj)
- [propertyTypeForUnknownKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2dn5xhizlyoqxxa4tpobsxe5dzkr4xazkgn5zfk3tlnzxxo3slmv4vaylunaxvg5dsnfxgolzikn2he2lom4wekt2fnz2gs5dzfe)
- [rawPageName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3smf3vaylhmvhgc3lff5jxi4tjnzts6kbj)
- [rawSystemPageName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3smf3vg6ltorsw2udbm5su4ylnmuxvg5dsnfxgolzife)
- [relationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3smvwgc5djn5xhg2djoaxukt2smvwgc5djn5xhg2djoaxsqu3uojuw4zzj)
- [sessionDidTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3tmvzxg2lpnzcgszcunfwwkt3voqxxm33jmqxsqtstjzxxi2lgnfrwc5djn5xcs)
- [setDynamicPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3tmv2ei6lomfwwsy2qmftwkl3wn5uwilzikn2he2lom4uq)
- [setEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3tmv2ek3tunf2hsl3wn5uwilziivhuk3tunf2hski)
- [setTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3tmv2fiyltnmxxm33jmqxsqu3uojuw4zzj)
- [takeValueForInferrableKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3umfvwkvtbnr2wkrtpojew4ztfojzgcytmmvfwk6jpozxwszbpfbhwe2tfmn2cyu3uojuw4zzj)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3un5jxi4tjnzts6u3uojuw4zzpfauq)
- [valueForKeyNoInference](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3wmfwhkzkgn5zewzlzjzxus3tgmvzgk3tdmuxu6ytkmvrxilzikn2he2lom4uq)
- [valueForKeyPathNoInference](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3wmfwhkzkgn5zewzlzkbqxi2con5ew4ztfojsw4y3ff5hwe2tfmn2c6kctorzgs3thfe)

Resolving Keys

- [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3umfvwkvtbnr2wkrtpojfwk6jpozxwszbpfbhwe2tfmn2cyu3uojuw4zzj)
- [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3umfvwkvtbnr2wkrtpojfwk6kqmf2gql3wn5uwilzij5rguzldoqwfg5dsnfxgoki)
- [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3wmfwhkzkgn5zewzlzf5hwe2tfmn2c6kctorzgs3thfe)
- [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3wmfwhkzkgn5zewzlzkbqxi2bpj5rguzldoqxsqu3uojuw4zzj)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2WContext__

public D2WContext()

Standard Java no-argument constructor.

---

__com.apple.yellow.directtoweb.D2WContext__

public D2WContext(D2WContext d2wContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__com.apple.yellow.directtoweb.D2WContext__

D2WContext(Settings settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__com.apple.yellow.directtoweb.D2WContext__

public D2WContext(WOSession session)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__NULL_VALUE__
java.lang.Object

This constant is intentionally undocumented.

---

__VALUE_TO_BE_DERIVED__
java.lang.Object

This constant is intentionally undocumented.

---

__Methods__

__attribute__

public EOAttribute attribute()

Returns the attribute (an EOAttribute object) corresponding to the current property in this Direct to Web context. Returns `null` if the property is not an attribute.

The EOAttribute class is define in the EOAccess Framework.

---

__attribute__

protected EOAttribute attribute(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__clearDerivedValues__

public void clearDerivedValues()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentClassPresentInRuntime__

public boolean componentClassPresentInRuntime(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentName__

public String componentName()

Returns the name of the property-level component to display based on the receiver's current property. The value is resolved using the rule system.

---

__componentsAvailable__

public Vector componentsAvailable()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__computeDerivedValues__

public void computeDerivedValues()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__displayNameForProperty__

public String displayNameForProperty()

Returns a String containing a user-presentable name for the receiver's current property. This value is resolved using the rule system.

---

__distantAttribute__

public EOAttribute distantAttribute(String aString, EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__distantRelationship__

public EORelationship distantRelationship(String aString, EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dynamicPage__

public String dynamicPage()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__entity__

public EOEntity entity()

Returns the receiver's current entity.

---

__frame__

public boolean frame()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inferAllPossibleValuesForKey__

public Vector inferAllPossibleValuesForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inferSystemValueForKey__

public Object inferSystemValueForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inferValueForKey__

public Object inferValueForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isGenerating__

public boolean isGenerating()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__keyWhenRelationship__

public String keyWhenRelationship()

When the receiver's current property is a relationship, returns the key for a property of the destination entity that identifies the entity. For example, if the receiver's current entity is `Movie` and the current property is the `toStudio` relationship (and thus the destination entity is `Studio`), an appropriate value for `keyWhenRelationship` is `name` since the `name` property identifies the studio.

---

__model__

public D2WModel model()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__nullOutDerivedValues__

public void nullOutDerivedValues()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__pageName__

public String pageName()

Returns the name of the Direct to Web template based on the receiver's current task and entity. This value is resolved using the rule system.

---

__pagesAvailable__

public Vector pagesAvailable()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyKey__

public String propertyKey()

Returns the key corresponding to the receiver's current property.

---

__propertyKeyIsKeyPath__

public boolean propertyKeyIsKeyPath()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyType__

public int propertyType()

Returns a String describing the type of the receiver's current property. Returns "r" if the property is a relationship, "a" if the property is an attribute, "c" if the property is a custom property, and "k" if the property is a key path.

---

__propertyTypeForUnknownKeyPath__

static public String propertyTypeForUnknownKeyPath(String aString, EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__rawPageName__

public String rawPageName()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__rawSystemPageName__

public String rawSystemPageName()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__relationship__

public EORelationship relationship()

Returns a relationship (an EORelationship object) for the receiver's in the Direct to Web context. Returns `null` if the property is not a relationship.

The EORelationship class is defined in the EOAccess Framework.

---

__relationship__

protected EORelationship relationship(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__sessionDidTimeOut__

public void sessionDidTimeOut(NSNotification notification)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDynamicPage__

public void setDynamicPage(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setEntity__

public void setEntity(EOEntity entity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setPropertyKey__

public void setPropertyKey(String newPropertyKey)

Sets the property key in the receiver's dictionary to `newPropertyKey`. This method is usually invoked by a Direct to Web template. See the "Direct to Web Architecture" chapter of _Developing WebObjects Applications With Direct To Web_ for more information.

---

__setTask__

public void setTask(String newTask)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__startupEntityName__

public String startupEntityName()

Returns a String containing the name of the entity to use in the startup page. The startup page (a query-all page by default) is the page created by the D2W `defaultPage` method and is the first page displayed after the user logs into an application generated by the Direct to Web wizard.

This key is resolved using the rule engine. With the default set of rules, this method returns an empty string because the query-all page does not work with any particular entity.

__See Also:__[defaultPage](D2W.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwizlgmf2wy5cqmftwkl2xj5bw63lqn5xgk3tuf4ufot2tmvzxg2lpnyuq) ([D2W](D2W.md))

---

__startupTask__

public String startupTask()

Returns a String containing the name of the application's startup page task ("queryAll" by default). The startup page is the page created by D2W `defaultPage` method and is the first page displayed after the user logs into an application generated by the Direct to Web wizard.

This key is resolved using the rule engine.

__See Also:__[defaultPage](D2W.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwizlgmf2wy5cqmftwkl2xj5bw63lqn5xgk3tuf4ufot2tmvzxg2lpnyuq) ([D2W](D2W.md))

---

__takeValueForInferrableKey__

public void takeValueForInferrableKey(Object anObject, String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__takeValueForKey__

public void takeValueForKey(Object newValue, String key)

Sets the receiver's value for `key` to be `newValue`. For a list of the keys implemented by D2WContext, see [Direct to Web Context Keys](Direct%20to%20Web%20Context%20Keys.md).

---

__takeValueForKeyPath__

public void takeValueForKeyPath(Object newValue, String keyPath)

Sets the receiver's value for the key path `keyPath` to `newValue`. For a list of the keys implemented by D2WContext, see [Direct to Web Context Keys](Direct%20to%20Web%20Context%20Keys.md).

---

__task__

public String task()

Returns a String containing the name of the receiver's current task.

---

__toString__

public String toString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__valueForKey__

public Object valueForKey(String key)

Returns the receiver's value (an Object) for `key`. This method may resolve the key using the rule system. For an explanation of how you use this method and a list of the keys implemented by D2WContext, see [Direct to Web Context Keys](Direct%20to%20Web%20Context%20Keys.md).

---

__valueForKeyNoInference__

public Object valueForKeyNoInference(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__valueForKeyPath__

public Object valueForKeyPath(String keyPath)

Returns the receiver's value (an Object) for the key path `keyPath`. This method enables you to access Direct to Web context keys paths such as `entity.name`. For an explanation of how you use this method, how the method resolves the key, and a list of the keys implemented by D2WContext, see [Direct to Web Context Keys](Direct%20to%20Web%20Context%20Keys.md).

__See Also:__[valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tumv4hil3wmfwhkzkgn5zewzlzf5hwe2tfmn2c6kctorzgs3thfe)

---

__valueForKeyPathNoInference__

public Object valueForKeyPathNoInference(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

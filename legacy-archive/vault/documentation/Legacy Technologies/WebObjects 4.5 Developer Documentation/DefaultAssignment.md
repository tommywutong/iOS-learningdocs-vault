---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/DefaultAssignment.html
archived_at: '2026-07-15T08:11:30.648135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__DefaultAssignment__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:[Assignment](Assignment.md)

---

__Class Description__

---

This class provides several methods that provide default values for the right-hand sides of rules. Many of these default values depend on the current entity or property in the Direct to Web context that is active when the rule fires.

DefaultAssignment is also a convenient class to subclass if you want to add your own assignment methods. To do so, subclass DefaultAssignment and add the method. Any rule that uses the method must have its right-hand-side value set to the name of the method. Use the `_context` variable to access the Direct to Web context that is active when the rule fires.

For more information about subclassing DefaultAssignment, see the "Customizing a Direct to Web Application" chapter of _Developing WebObjects Applications with Direct to Web_.

__Method Types__

---

Constructors

- [public DefaultAssignment(String keyPath, String value)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5cgkztbovwhiqltonuwo3tnmvxhil2emvtgc5lmoraxg43jm5xg2zlooqxsqu3uojuw4zzmkn2he2lom4uq)
- [public DefaultAssignment(EOKeyValueUnarchiver unarchiver)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5cgkztbovwhiqltonuwo3tnmvxhil2emvtgc5lmoraxg43jm5xg2zlooqxsqrkpjnsxsvtbnr2wkvlomfzgg2djozsxeki)

---

Firing the Rule

- [fire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5tgs4tff5hwe2tfmn2c6kcegjlug33oorsxq5bj)

Private Methods

- [attributeWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5qxi5dsnfrhk5dfk5uwi5dif5uw45bpfauq)
- [valueString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf53gc3dvmvjxi4tjnzts6u3uojuw4zzpfauq)

Providing Default Values

- [defaultDisplayNameForProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5sgkztbovwhirdjonygyylzjzqw2zkgn5zfa4tpobsxe5dzf5jxi4tjnzts6kbj)
- [defaultEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5sgkztbovwhirlooruxi6komfwwkl2torzgs3thf4ucs)
- [defaultPropertyKeysFromEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5sgkztbovwhiudsn5ygk4tupffwk6ltizzg63kfnz2gs5dzf5hfgqlsojqxslzife)
- [defaultPropertyKeysFromEntityWithoutRelationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5sgkztbovwhiudsn5ygk4tupffwk6ltizzg63kfnz2gs5dzk5uxi2dpov2fezlmmf2gs33oonugs4dtf5hfgqlsojqxslzife)
- [isEntityReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5uxgrlooruxi6ksmvqwit3onr4s6sloorswozlsf4ucs)
- [smartDefaultAttributeWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhiqluorzgsytvorsvo2leoruc6u3uojuw4zzpfauq)
- [smartDefaultAttributeWidthAsInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhiqluorzgsytvorsvo2leoruec42jnz2c62looqxsqki)
- [smartDefaultEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhirlooruxi6komfwwk4zpjzjuc4tsmf4s6kbj)
- [smartDefaultKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhis3fpexvg5dsnfxgolzife)
- [smartDefaultKeyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhis3fpflwqzlokjswyylunfxw443infyc6u3uojuw4zzpfauq)
- [smartDefaultRows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhiutpo5zs6u3uojuw4zzpfauq)

---

__Constructors__

---

__com.apple.yellow.directtoweb.DefaultAssignment__

public DefaultAssignment(String keyPath, String value)

Creates a DefaultAssignment object and sets its key path and value.

---

__com.apple.yellow.directtoweb.DefaultAssignment__

public DefaultAssignment(EOKeyValueUnarchiver unarchiver)

Creates a DefaultAssignment object based on a EOKeyValueUnarchiver object. You use this constructor to read the assignment information from a rule file.

---

__Methods__

__attributeWidth__

public int attributeWidth()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__defaultDisplayNameForProperty__

public String defaultDisplayNameForProperty()

Returns a String containing a user-presentable version of the current property key in the Direct to Web context in which the receiver's rule fires. This string is formed by capitalizing the key and inserting spaces between words with mixed case.

---

__defaultEntityName__

public String defaultEntityName()

Returns the first entity name in the NSArray returned by `smartDefaultEntityNames`.

__See Also:__[smartDefaultEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhirlooruxi6komfwwk4zpjzjuc4tsmf4s6kbj)

---

__defaultPropertyKeysFromEntity__

public NSArray defaultPropertyKeysFromEntity()

Returns a sorted NSArray containing the property keys for the current entity excluding primary and foreign keys.

---

__defaultPropertyKeysFromEntityWithoutRelationships__

public NSArray defaultPropertyKeysFromEntityWithoutRelationships()

Returns a sorted NSArray containing the property keys for the current entity excluding relationships, primary keys, and foreign keys.

---

__fire__

public synchronized Object fire(D2WContext context)

This method is invoked when the receiver's rule fires. In turn, it invokes the method in this class specified by the receiver's right-hand-side value.

---

__isEntityReadOnly__

public Integer isEntityReadOnly()

Returns whether or not the current entity (in the Direct to Web context in which the receiver's rule fires) can be modified. You can specify if an entity can be modified using the Web Assistant. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more details.

You can override this method to provide your own criteria for whether or not a entity can be modified.

---

__smartDefaultAttributeWidth__

final public String smartDefaultAttributeWidth()

Returns a String containing the result of `smartDefaultAttributeWidthAsInt`.

__See Also:__[smartDefaultAttributeWidthAsInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3duifzxg2lhnzwwk3tuf5zw2ylsorcgkztbovwhiqluorzgsytvorsvo2leoruec42jnz2c62looqxsqki)

---

__smartDefaultAttributeWidthAsInt__

public int smartDefaultAttributeWidthAsInt()

Returns the width of the current attribute in the Direct to Web context in which the receiver's rule fires. Returns 50 if the width of the current attribute is less than 50. Returns 20 if the current property is not an attribute.

---

__smartDefaultEntityNames__

public final NSArray smartDefaultEntityNames()

Returns a sorted NSArray containing the names of the entities in the application. Entities having fewer than three relationships and no attributes are assumed to be join tables and are excluded.

---

__smartDefaultKey__

public String smartDefaultKey()

Returns the key for the default property of the current entity in the Direct to Web context in which the receiver's rule fires. This method guesses the most likely property with which the user will query for the entity and returns its key.

---

__smartDefaultKeyWhenRelationship__

public String smartDefaultKeyWhenRelationship()

Returns a key for the default property of the current relationship's destination object. If the current property (in the Direct to Web context in which the receiver's rule fires) is not a relationship, returns `null`. This method guesses the most likely property with which the user will query for the relationship's destination entity and returns its key.

---

__smartDefaultRows__

final public String smartDefaultRows()

Returns a String containing an estimate of the number of rows that a WOText element would need to display the current attribute.

---

__valueString__

public String valueString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

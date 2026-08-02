---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtPropertyIntrospection.html
archived_at: '2026-07-15T07:17:29.386173Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Type%20Encodings.md)

# 声明属性

当编译器遇到属性声明（参见 _[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中的 [声明属性](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17)）时，它会生成与所在的类、分类或协议相关联的描述性元数据。你可以通过一组函数访问这些元数据，它们支持按名称在类或协议上查找属性、以 `@encode` 字符串的形式获取属性的类型，以及把属性的特性列表复制成一个 C 字符串数组。每个类和协议都有一份可用的声明属性列表。

`Property` 结构定义了一个指向属性描述符的不透明句柄。

```c
typedef struct objc_property *Property;
```

你可以分别用 `class_copyPropertyList` 和 `protocol_copyPropertyList` 函数取回与某个类（包括已加载的分类）以及某个协议相关联的属性数组：

```c
objc_property_t *class_copyPropertyList(Class cls, unsigned int *outCount)
objc_property_t *protocol_copyPropertyList(Protocol *proto, unsigned int *outCount)
```

例如，给定下面这个类声明：

```objc
@interface Lender : NSObject {
    float alone;
}
@property float alone;
@end
```

你可以这样获取属性列表：

```objc
id LenderClass = objc_getClass("Lender");
unsigned int outCount;
objc_property_t *properties = class_copyPropertyList(LenderClass, &outCount);
```

你可以用 `property_getName` 函数得到一个属性的名称：

```c
const char *property_getName(objc_property_t property)
```

你可以分别用 `class_getProperty` 和 `protocol_getProperty` 函数，在类和协议中获取具有给定名称的属性的引用：

```c
objc_property_t class_getProperty(Class cls, const char *name)
objc_property_t protocol_getProperty(Protocol *proto, const char *name, BOOL isRequiredProperty, BOOL isInstanceProperty)
```

你可以用 `property_getAttributes` 函数得到一个属性的名称及其 `@encode` 类型字符串。关于编码类型字符串的详情，参见 [类型编码](Type%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgawvgvzr)；关于该字符串本身的详情，参见 [属性类型字符串](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgewvgvzw) 和 [属性特性描述示例](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgewvgvzv)。

```c
const char *property_getAttributes(objc_property_t property)
```

把这些结合起来，你就可以用下面的代码打印出与某个类相关联的所有属性：

```objc
id LenderClass = objc_getClass("Lender");
unsigned int outCount, i;
objc_property_t *properties = class_copyPropertyList(LenderClass, &outCount);
for (i = 0; i < outCount; i++) {
    objc_property_t property = properties[i];
    fprintf(stdout, "%s %s\n", property_getName(property), property_getAttributes(property));
}
```


你可以用 `property_getAttributes` 函数得到一个属性的名称、它的 `@encode` 类型字符串，以及该属性的其他特性。

该字符串以 `T` 开头，后跟 `@encode` 类型和一个逗号，并以 `V` 加上支撑该属性的实例变量名称结束。在两者之间，由下列描述符指定各项特性，彼此以逗号分隔：

__表 7-1__  声明属性的类型编码

| 编码 | 含义 |
| --- | --- |
| `R` | 该属性是只读的（`readonly`）。 |
| `C` | 该属性是最后所赋值的一份副本（`copy`）。 |
| `&` | 该属性是对最后所赋值的一个引用（`retain`）。 |
| `N` | 该属性是非原子的（`nonatomic`）。 |
| `G<name>` | 该属性定义了自定义的 getter 选择器名称。名称跟在 `G` 之后（例如 `GcustomGetter,`）。 |
| `S<name>` | 该属性定义了自定义的 setter 选择器名称。名称跟在 `S` 之后（例如 `ScustomSetter:,`）。 |
| `D` | 该属性是动态的（`@dynamic`）。 |
| `W` | 该属性是一个弱引用（`__weak`）。 |
| `P` | 该属性符合垃圾回收的条件。 |
| `t<encoding>` | 使用旧式编码指定类型。 |

示例参见 [属性特性描述示例](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgewvgvzv)。

给定这些定义：

```c
enum FooManChu { FOO, MAN, CHU };
struct YorkshireTeaStruct { int pot; char lady; };
typedef struct YorkshireTeaStruct YorkshireTeaStructType;
union MoneyUnion { float alone; double down; };
```

下表展示了一些属性声明的示例，以及 `property_getAttributes` 返回的相应字符串：

| 属性声明 | 属性描述 |
| --- | --- |
| `@property char charDefault;` | `Tc,VcharDefault` |
| `@property double doubleDefault;` | `Td,VdoubleDefault` |
| `@property enum FooManChu enumDefault;` | `Ti,VenumDefault` |
| `@property float floatDefault;` | `Tf,VfloatDefault` |
| `@property int intDefault;` | `Ti,VintDefault` |
| `@property long longDefault;` | `Tl,VlongDefault` |
| `@property short shortDefault;` | `Ts,VshortDefault` |
| `@property signed signedDefault;` | `Ti,VsignedDefault` |
| `@property struct YorkshireTeaStruct structDefault;` | `T{YorkshireTeaStruct="pot"i"lady"c},VstructDefault` |
| `@property YorkshireTeaStructType typedefDefault;` | `T{YorkshireTeaStruct="pot"i"lady"c},VtypedefDefault` |
| `@property union MoneyUnion unionDefault;` | `T(MoneyUnion="alone"f"down"d),VunionDefault` |
| `@property unsigned unsignedDefault;` | `TI,VunsignedDefault` |
| `@property int (*functionPointerDefault)(char *);` | `T^?,VfunctionPointerDefault` |
| `@property id idDefault;`  注意：编译器会警告：`"no 'assign', 'retain', or 'copy' attribute is specified - 'assign' is assumed"` | `T@,VidDefault` |
| `@property int *intPointer;` | `T^i,VintPointer` |
| `@property void *voidPointerDefault;` | `T^v,VvoidPointerDefault` |
| `@property int intSynthEquals;`  在实现块中：  `@synthesize intSynthEquals=_intSynthEquals;` | `Ti,V_intSynthEquals` |
| `@property(getter=intGetFoo, setter=intSetFoo:) int intSetterGetter;` | `Ti,GintGetFoo,SintSetFoo:,VintSetterGetter` |
| `@property(readonly) int intReadonly;` | `Ti,R,VintReadonly` |
| `@property(getter=isIntReadOnlyGetter, readonly) int intReadonlyGetter;` | `Ti,R,GisIntReadOnlyGetter` |
| `@property(readwrite) int intReadwrite;` | `Ti,VintReadwrite` |
| `@property(assign) int intAssign;` | `Ti,VintAssign` |
| `@property(retain) id idRetain;` | `T@,&,VidRetain` |
| `@property(copy) id idCopy;` | `T@,C,VidCopy` |
| `@property(nonatomic) int intNonatomic;` | `Ti,VintNonatomic` |
| `@property(nonatomic, readonly, copy) id idReadonlyCopyNonatomic;` | `T@,R,C,VidReadonlyCopyNonatomic` |
| `@property(nonatomic, readonly, retain) id idReadonlyRetainNonatomic;` | `T@,R,&,VidReadonlyRetainNonatomic` |

[下一页](Document%20Revision%20History.md)[上一页](Type%20Encodings.md)


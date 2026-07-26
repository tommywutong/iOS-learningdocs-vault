# SQLite使用质量检测
## 前言
SQLite在移动端开发中广泛使用，其使用质量直接影响到产品的体验。微信是个重度使用SQLite的应用，相关的质量检测也是质量监控体系中不可忽视的一部分。  
常见的SQLite质量监控一般都是依赖上线后反馈的机制，比如耗时监控或者用户反馈。这种方式问题是：

* 事后发现，负面影响已经发生。
* 关注的只是没这么差。eg.监控阈值为500ms，那么一条可优化为20ms而平均耗时只有490ms的sql就被忽略了。

能否在上线前就进行SQLite使用质量的监控？于是我们尝试开发了一个工具：**SQLiteLint**。虽然名带“lint”，但并不是代码的静态检查，而是在APP运行时对sql语句、执行序列、表信息等进行分析检测。而和“lint”有点类似的是：在开发阶段就介入，并运用一些最佳实践的规则来检测，从而发现潜在的、可疑的SQLite使用问题。  

本文会介绍SQLiteLint的思路，也算是SQLite使用经验的分享，希望对大家有所帮助。

## 简述
**SQLiteLint在APP运行时进行检测，而且大部分检测算法与数据量无关即不依赖线上的数据状态。只要你触发了某条sql语句的执行，SQLiteLint就会帮助你review这条语句是否写得有问题。而这在开发、测试或者灰度阶段就可以进行。**
  
检测流程十分简单：

![flow-process diagram](https://mmbiz.qpic.cn/mmbiz_png/4wQxza4CwrRf3lpccSOLTzhJPyBNPj6Urle8RTp2ZDTDQbbzeSeEpHRut08Ic3AmGu2Sm6M1QnMYkPQmm9eqicg/640?wx_fmt=png)   

1. 收集APP运行时的sql执行信息  
包括执行语句、创建的表信息等。其中表相关信息可以通过pragma命令得到。对于执行语句，有两种情况：   
a) DB框架提供了回调接口。比如微信使用的是WCDB，很容易就可以通过MMDataBase.setSQLiteTrace 注册回调拿到这些信息。  
b) 若使用Android默认的DB框架，SQLiteLint提供了一种无侵入的获取到执行的sql语句及耗时等信息的方式。通过hook的技巧，向SQLite3 C层的api sqlite3_profile方法注册回调，也能拿到分析所需的信息，从而无需开发者额外的打点统计代码。
2. 预处理  
包括生成对应的sql语法树，生成不带实参的sql，判断是否select*语句等，为后面的分析做准备。预处理和后面的算法调度都在一个单独的处理线程。  
3. 调度具体检测算法执行  
checker就是各种检测算法，也支持扩展。并且检测算法都是以C++实现，方便支持多平台。而调度的时机包括：最近未分析sql语句调度，抽样调度，初始化调度，每条sql语句调度。  
4. 发布问题  
上报问题或者弹框提示。

可以看到重点在第3步，下面具体讨论下SQLiteLint目前所关注的质量问题检测。

## 检测问题简介
### 一、检测索引使用问题
索引的使用问题是数据库最常见的问题，也是最直接影响性能的问题。SQLiteLint的分析主要基于SQLite3的"explain query plan"，即sql的查询计划。先简单说下查询计划的最常见的几个关键字：

---

**SCAN TABLE**:全表扫描，遍历数据表查找结果集，复杂度O(n)  
**SEARCH TABLE**:利用索引查找，一般除了without rowid表或覆盖索引等，会对索引树先一次Binary Search找到rowid，然后根据得到rowid去数据表做一次Binary Search得到目标结果集，复杂度为O(logn)  
**USE TEMP B-TREE**:对结果集临时建树排序，额外需要空间和时间。比如有Order By关键字，就有可能出现这样查询计划

---

通过分析查询计划，SQLiteLint目前主要检查以下几个索引问题：  

* **未建索引导致的全表扫描**（对应查询计划的SCAN TABLE...）   

虽然建立索引是最基本优化技巧，但实际开发中，很多同学因为意识不够或者需求太紧急，而疏漏了建立合适的索引，SQLiteLint帮助提醒这种疏漏。问题虽小，解决也简单，但最普遍存在。  
这里也顺带讨论下一般不适合建立索引的情况：写多读少以及表行数很小。但对于客户端而言，写多读少的表应该不常见。而表行数很小的情况，建索引是有可能导致查询更慢的（因为索引的载入需要的时间可能大过全表扫描了），但是这个差别是微乎其微的。所以这里认为一般情况下，客户端的查询还是尽量使用索引优化，如果确定预估表数量很小或者写多读少，也可以将这个表加到不检测的白名单。

解决这类问题，当然是建立对应的索引。
  
* **索引未生效导致的全表扫描**（对应查询计划的SCAN TABLE...）  

有些情况即便建立了索引，但依然可能不生效，而这种情况有时候是可以通过优化sql语句去用上索引的。举个例子：

```
sqlite> pragma table_info('t');
0|name|text|0||0
1|age|integer|0||0
sqlite> pragma index_list('t');
0|nameIndex|0|c|0
sqlite> explain query plan select age from t where name like 'lo%';
0|0|0|SCAN TABLE t
```
以上看到，即便已建立了索引，但实际没有使用索引来查询。  
如对于这个case，可以把like变成不等式的比较：

```
sqlite> explain query plan select age from t where name >= 'lo' and name < 'lp';
0|0|0|SEARCH TABLE t USING INDEX nameIndex (name>? AND name<?)
```
这里看到已经是使用索引来SEARCH TABLE，避免了全表扫描。但值得注意的是并不是所有like的情况都可以这样优化，如like '%lo' 或 like '%lo%' ，不等式就做不到了。  

再看个位操作导致索引不生效的例子：  

```
sqlite> pragma table_info('t0');
0|id|integer|0||1
1|flag|integer|0||0
sqlite> pragma index_list('t0');
0|flagIndex|0|c|0
sqlite> explain query plan select id from t0 where flag&0x1!=0 and flag&0x4!=0;
0|0|0|SCAN TABLE t0
```
位操作是最常见的导致索引不生效的语句之一。但有些时候也是有些技巧的利用上索引的，假如这个case里flag的业务取值只有0x1，0x2，0x4，0x8，那么这条语句就可以通过穷举值的方式等效：

```
sqlite> explain query plan select id from t0 where flag in (5,7,13,15);
0|0|0|SEARCH TABLE t0 USING COVERING INDEX flagIndex (flag=?)
0|0|0|EXECUTE LIST SUBQUERY 1
```
以上看到，把位操作转成in穷举就能利用索引了。

解决这类 索引未生效导致的全表扫描 的问题，需要结合实际业务好好优化sql语句，甚至使用一些比较trick的技巧。也有可能没办法优化，这时需要添加到白名单。

* **不必要的临时建树排序**（对应查询计划的USE TEMP B-TREE...)。

比如sql语句中order by、distinct、group by等就有可能引起对结果集临时额外建树排序，当然很多情况都是可以通过建立恰当的索引去优化的。举个例子：

```
sqlite> pragma table_info('t1');
0|id|integer|0||0
1|mark|integer|0||0
sqlite> pragma index_list('t1');
0|markIndex|0|c|0
1|idIndex|0|c|0
sqlite> explain query plan select * from t1 where mark = 60 order by id limit 1;
0|0|0|SEARCH TABLE t1 USING INDEX markIndex (mark=?)
0|0|0|USE TEMP B-TREE FOR ORDER BY
```
以上看到，即便id和mark都分别建立了索引，即便只需要一行结果，依然会引起重新建树排序（USE TEMP B-TREE FOR ORDER BY）。当然这个case非常简单，不过如果对SQLite的索引不熟悉或者开发时松懈了，确实很容易发生这样的问题。同样这个问题也很容易优化:  

```
sqlite> create index if not exists markIdIndex on t1(mark, id);
sqlite> explain query plan select * from t1 where mark = 60 order by id limit 1;
0|0|0|SEARCH TABLE t1 USING COVERING INDEX markIdIndex (mark=?)
```
这样就避免了重新建树排序，这对于数据量大的表查询，优化效果是立竿见影的好。

解决这类问题，一般就是建立合适的索引。

* **不足够的索引组合**

这个主要指已经建立了索引，但索引组合的列并没有覆盖足够where子句的条件式中的列。SQLiteLint检测出这种问题，建议先关注该sql语句是否有性能问题，再决定是否建立一个更长的索引。举个例子：

```
sqlite> pragma table_info('t2');
0|name|text|0||0
1|gender|integer|0||0
2|mark|integer|0||0
sqlite> pragma index_list('t2');
0|genderIndex|0|c|0
sqlite> explain query plan select name from t2 where gender=1 and mark=60;
0|0|0|SEARCH TABLE t2 USING INDEX genderIndex (gender=?)
```

***

以上看到，确实是利用了索引genderIndex来查询，但看到where子句里还有一个mark=60的条件，所以还有一次遍历判断操作才能得到最终需要的结果集。尤其对于这个case，gender也就是性别，那么最多**3**种情况，这个时候单独的gender索引的优化效果的已经不明显了。而同样，优化也是很容易的：

```
sqlite> create index if not exists markGenderIndex on t2(mark, gender);
sqlite> explain query plan select name from t2 where gender=1 and mark=60;
0|0|0|SEARCH TABLE t2 USING INDEX markGenderIndex (mark=? AND gender=?)
``` 

解决这类问题，一般就是建立一个更大的组合索引。

* **怎么降低误报**

现在看到SQLiteLint主要根据查询计划的某些关键字去发现这些问题，但SQLite支持的查询语法是非常复杂的，而对应的查询计划也是无穷变化的。**所以对查询计划自动且正确的分析，不是一件容易的事。SQLiteLint很大的功夫也在这件事情上**。SQLiteLint这里主要对输出的查询计划重新构建了一棵有一定的特点的分析树，并结合sql语句的语法树，依据一定的算法及规则进行分析检测。建分析树的过程会使用到每条查询计划前面如"0|1|0"的数字，这里不具体展开了。  
举个例子：是不是所有带有"SCAN TABLE"前缀的查询计划，都认为是需要优化的呢？明显不是。具体看个case：  

```  
sqlite> pragma index_list('t3');  
0|idIndex|0|c|0  
sqlite> pragma index_list('t4');  
sqlite> explain query plan select t4.name from t3,t4 where t3.id=t4.id;  
0|0|1|SCAN TABLE t4
0|1|0|SEARCH TABLE t3 USING COVERING INDEX idIndex (id=?)
```
这是一个联表查询，在SQLite的实现里一般就是嵌套循环。在这个语句中里，t3.id列建了索引，并且在第二层循环中用上了，但第一层循环的SCAN TABLE是无法优化的。比如尝试给t4的id列也建立索引：

```
sqlite> pragma index_list('t4');
0|t4IdIndex|0|c|0
sqlite> explain query plan select t4.name from t3,t4 where t3.id=t4.id;
0|0|1|SCAN TABLE t4
0|1|0|SEARCH TABLE t3 USING COVERING INDEX idIndex (id=?)
```
可以看出,依然无法避免SCAN TABLE。对于这种SCAN TABLE无法优化的情况，SQLiteLint不应该误报。前面提到，会对查询计划组织成树的结构。比如对于这个case，最后构建的查询计划分析树为：

![flow-process diagram](https://mmbiz.qpic.cn/mmbiz_png/4wQxza4CwrRf3lpccSOLTzhJPyBNPj6UF1RlBDzDs6JygPmfUI6sVjOroAwgVKpJD6j9qcuFvFnDPh9SBa7M5w/640?wx_fmt=png)

分析树，有个主要的特点：叶子节点有兄弟节点的是联表查询，其循环顺序对应从左往右，而无兄弟节点是单表查询。而最后的分析会落地到叶子节点的分析。遍历叶子节点时，有一条规则（不完整描述）是：

*叶子节点有兄弟节点的，且是最左节点即第一层循环，且where子句中不含有相关常量条件表达式时，SCAN TABLE不认为是质量问题。*

这里有两个条件必须同时满足，SCAN TABLE才不报问题：第一层循环 & 无相关常量表达式。第一层循环前面已经描述，这里再解释下后面一个条件。

```
sqlite> explain query plan select t4.name from t3,t4 where t3.id=t4.id and t4.id=666;
0|0|1|SEARCH TABLE t4 USING INDEX t4IdIndex (id=?)
0|1|0|SEARCH TABLE t3 USING COVERING INDEX idIndex (id=?)
```

由上看到,当select子句中出现常量条件表达式“t4.id=666”, 若t3.id,t4.id都建了索引，是可以优化成没有SCAN TABLE。

```
sqlite> drop index t4IdIndex;
sqlite> explain query plan select t4.name from t3,t4 where t3.id=t4.id and t4.id=666;
0|0|1|SCAN TABLE t4
0|1|0|SEARCH TABLE t3 USING COVERING INDEX idIndex (id=?)
```
而把t4.id的索引删除后，又出现了SCAN TABLE。而这种SCAN TABLE的情况，不满足规则里的的第二个条件，SQLiteLint就会报出可以使用索引优化了。

这里介绍了一个较简单语句的查询计划的分析，当然还有更复杂的语句，还有子查询、组合等等，这里不展开讨论了。巨大的复杂性，无疑对准确率有很大的挑战，需要对分析规则不断地迭代完善。当前SQLiteLint的分析算法依然不足够严谨，还有很大的优化空间。  
这里还有另一个思路去应对准确性的问题：对所有上报的问题，结合耗时、是否主线程、问题等级等信息，进行优先级排序。这个“曲线救国”来降低误报的策略也适用本文介绍的所有检测问题。

### 二、检测冗余索引问题
SQLiteLint会在应用启动后对所有的表检测一次是否存在冗余索引，并建议保留最大那个索引组合。 

先定义什么是冗余索引：如对于某个表，如果索引组合index1，index2是另一个索引组合index3的前缀，那么一般情况下index3可以替代掉index1和index2的作用，所以index1，index2就冗余了。而**多余的索引就会有多余的插入消耗和空间消耗**，一般就建议只保留索引index3。
看个例子：

```
sqlite> pragma index_list('t3');
0|lengthTypeIndex|0|c|0
sqlite> pragma index_info('lengthTypeIndex');
0|1|length
1|2|type
sqlite> explain query plan select id from t3 where length=5;
0|0|0|SEARCH TABLE t3 USING INDEX lengthTypeIndex (length=?)
```
以上看到，如果已经有一个length和type的组合索引，就已经满足了单length列条件式的查询，没必要再为length再建一个索引。   

### 三、检测select * 问题
SQLiteLint这里通过扫描sql语法树，若发现select * 子句，就会报问题，建议尽量避免使用select * ，而是按需select对应的列。  

select * 是SQLite最常用的语句之一，也非常方便，为什么还认为是问题的呢？这里有必要辩驳一下： 
 
1. 对于select * ，SQLite底层依然存在一步把 * 展开成表的全部列。  
2. select * 也减少了可以使用覆盖索引的机会。覆盖索引指索引包含的列已经覆盖了select所需要的列，而使用上覆盖索引就可以减少一次数据表的查询。  
3. 对于Android平台而言，select * 就会投射所有的列，那么每行结果占据的内存就会相对更大，那么CursorWindow（缓冲区）的容纳条数就变少，那么SQLiteQuery.fillWindow的次数就可能变多，这也有一定的性能影响。
  
基于以上原因，出于SQLiteLint目标最佳实践的原则，这里依然报问题。  

### 四、检测Autoincrement问题
SQLiteLint在应用启动后会检测一次所有表的创建语句，发现 AUTOINCREMENT关键字，就会报问题，建议避免使用Autoincrement。  
  
这里看下为什么要检测这个问题，下面引用SQLite的官方文档：
> The AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.

可以看出Auto Increment确实不是个好东西。  
ps. 我这里补充说明一下 strictly needed是什么是意思，也就是为什么它不必要。通常AUTOINCREMENT用于修饰INTEGER PRIMARY KEY列，后简称IPK列。而IPK列等同于rowid别名，本身也具有自增属性，但会复用删除的rowid号。比如当前有4行，最大的rowid是4，这时把第4行删掉，再插入一行，新插入行的rowid取值是比当前最大的rowid加1，也就3+1=4，所以复用了rowid号4。而如果加以AUTOINCREMENT修饰就是阻止了复用，在这个情况，rowid号是5。也就是说，AUTOINCREMENT可以保证了历史自增的唯一性，但对于客户端应用有多少这样的场景呢？

### 五、检测建议使用prepared statement
SQLiteLint会以抽样的时机去检测这个问题，比如每50条执行语句，分析一次执行序列，如果发现连续执行次数超过一定阈值的相同的（当然实参可以不同）而未使用prepared statement的sql语句，就报问题，建议使用prepared statement优化。  
如阈值是3，那么连续执行下面的语句，就会报问题：

```
insert into t(name, age) values('a', 10);
insert into t(name, age) values('b', 11);
insert into t(name, age) values('c', 15);
```

使用prepared statement优化的好处有两个：

1. 对于相同（实参不同）的sql语句多次执行，会有性能提升
2. 如果参数是不可信或不可控输入，还防止了注入问题

### 六、检测建议使用without rowid特性
SQLiteLint会在应用启动后检测一次所有表的创建语句，发现未使用without rowid技巧且根据表信息判断适合使用without rowid优化的表，就报问题，建议使用without rowid优化。  
这是SQLiteLint的另一个思路，就是发现是否可以应用上一些SQLite的高级特性。

without rowid在某些情况下可以同时带来空间以及时间上将近一半的优化。简单说下原理，如：  

```
sqlite> create table t4(name text primary key, mark integer);
sqlite> select mark from t4 where name='lo';
```

对于这个含有rowid的表（rowid是自动生成的），这时这里涉及到两次查询，一次在name的索引树上找到对应的rowid，一次是用这个rowid在数据树上查询到mark列。  
而使用without rowid来建表：  

```
sqlite> create table t4(name text primary key, mark integer) without rowid;
```

数据树构建是以name为key，mark为data的，并且是以普通B-tree的方式存储。这样对于刚刚同样的查询，就需要只有一次数据树的查询就得到了mark列，所以算法复杂度上已经省了一个O(logn）。另外又少维护了一个name的索引树，插入消耗和空间上也有了节省。

当然withou rowid不是处处适用的，不然肯定是默认属性了。SQLiteLint判断如果同时满足以下两个条件，就建议使用without rowid：  

1. 表含有non-integer or composite (multi-column) PRIMARY KEY
2. 表每行数据大小不大，一个比较好的标准是行数据大小小于二十分之一的page size。ps.默认page size SQLite版本3.12.0以后（对应Android O以上）是4096 bytes，以前是1024。而由于行数据大小业务相关，为了降低误报，SQLiteLint使用更严格的判定标准：表不含有BLOB列且不含有非PRIMARY KEY TEXT列。

简单说下原因：  
对于1，假如没有PRIMARY KEY，无法使用without rowid特性；假如有INTEGER PRIMARY KEY，前面也说过，这时也已经等同于rowid。  
对于2，小于20分之一pagesize是官方给出的建议。  
这里说下我理解的原因。page是SQLite一般的读写单位（实际上磁盘的读写block更关键，而磁盘的消耗更多在定位上，更多的page就有可能需要更多的定位）。without rowid的表是以普通B-Tree存储的，而这时数据也存储在所有树结点上，那么假如数据比较大，一个page存储的结点变少，那么查找的过程就需要读更多的page，从而查找的消耗更大。当然这是相对rowid表B*-Tree的存储来说的，因为这时数据都在叶子结点，搜索路径上的结点只有KEY，那么一个page能存的结点就多了很多，查找磁盘消耗变小。这里注意的是，不要以纯内存的算法复杂度去考量这个问题。以上是推论不一定正确，欢迎指教。

引申一下，这也就是为什么SQLite的索引树以B-Tree组织，而rowid表树以B\*-Tree组织，因为索引树每个结点的存主要是索引列和rowid，往往没这么大，相对B\*-Tree优势就在于不用一直查找到叶子结点就能结束查找。与without rowid同样的限制，**不建议用大String作为索引列，这当然也可以加入到SQLiteLint的检测**。

## 小结
这里介绍了一个在开发、测试或者灰度阶段进行SQLite使用质量检测的工具，这个思路的好处是：

* 上线前发现问题
* 关注最佳实践

本文的较大篇幅其实是对SQLite最佳实践的讨论，因为SQLiteLint的思路就是对最佳实践的自动化检测。当然检查可以覆盖更广的范围，准确性也是挑战，这里还有很大的空间。  

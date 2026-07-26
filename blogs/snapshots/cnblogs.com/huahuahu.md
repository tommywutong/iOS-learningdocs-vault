---
title: huahuahu
source_url: 'https://www.cnblogs.com/huahuahu/p/sqlite-suo-yin-de-yuan-li-ji-ying-yong.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:2398ef48b3e899fd'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 2｜有了存储场景，再补数据库最低原理（对应 W6-15、W6-16）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 2｜有了存储场景，再补数据库最低原理（对应 W6-15、W6-16）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[huahuahu](https://www.cnblogs.com/huahuahu/p/sqlite-suo-yin-de-yuan-li-ji-ying-yong.html)

## 引言

[这篇文章](http://www.cnblogs.com/lyroge/p/3837886.html)，里面讲到对于一个41G大小、包含百万条记录的数据库进行查询操作，如果利用了索引，可以把操作耗时从37s降到0.2s。  
 那么什么是索引呢？利用索引可以加快数据库查询操作的原理是什么呢？

## 索引的基本原理

数据库提供了一种持久化的数据存储方式，从数据库中查询数据库是一个基本的操作，查询操作的效率是很重要的。  
 对于查询操作来说，如果被查询的数据已某种方式组织起来，那么查询操作的效率会极大提高。  
 在数据库中，一条记录会有很多列。如果把这些记录按照列Col1以某种数据结构组织起来，那么列Col2一定是乱序的。  
 因此，数据库在原始数据之外，维护了满足特定查找算法的数据结构，指向原始数据，称之为**索引**。  
 举例来说，在下面的图中，数据库有两列Col1、Col2。在存储时，按照列Col1组织各行，比如Col1已二叉树方式组织。如果查找col1中的某一个值，利用二叉树进行二分查找，不需要遍历整个数据库。  
 这样一来列Col2就是乱序的。为了解决这个问题，为Col2建立了索引，即把Col2也按照某种数据结构（这里是二叉树）组织起来。这样子查找列Col2时只需要进行二分查找即可。  
 ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000303698-1812536719.jpg)￼

## 索引的实现

由于数据库是存储在磁盘上的，因此实现索引用的数据结构会存储在磁盘上。磁盘的IO是需要注意的问题。

1. 二叉树  
   二叉树是一种经典的数据结构，但是并不适合进行数据库索引。  
   原因在于二叉树中每一个节点的度只有2，树的深度较高。在存储时，一般一个节点需要一次磁盘IO，树的深度较高，查询一个数据需要的磁盘IO次数越高，查找需要的时间越长。
2. B树  
   B树是二叉树的变种，主要区别在于每一个节点的度可以大于2，即每一个节点可以分很多叉，大大降低了树的深度。  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000259917-1381132805.jpg)￼

    - 每条数据表示为[key,data]
    - 每个非叶子节点有(n-1)条数据n个指针组成
    - 所有叶节点具有相同的深度，等于树高h
    - 指针指向节点的key大于左边的记录小于右边记录

  上面这些特点使得B+树的深度大大降低，并且实现了对数据的有序组织。
3. B+树  

   B+树是对B树的扩展，特点在于非叶子节点不存储data，只存储key。如果每一个节点的大小固定（如4k，正如在sqlite中那样），那么可以进一步提高内部节点的度，降低树的深度。  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000300573-1257836218.jpg)￼

    - 非叶子节点只存储key，叶子节点不存储指针
    - 每一个节点大小固定，需要一次读磁盘操作（page）
4. 顺序访问指针的B+树  

   对B+树做了一点改变，每一个叶子节点增加一个指向相邻叶子节点的指针，这样子可以提高区间访问的性能。  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000259979-1545142523.jpg)￼  
   如图，访问key在15到30的data。

    - 如果没有水平的指针  
       B+树查找找到key=15的data，在同一个块中找到key=18的data。然后进行第二次B+查找，找到key=20的data，在同一个块中找到key=30的data。
    - 有水平的指针  
       B+树查找找到key=15的data，查找同一个块的内容，或沿着水平指针依次向右遍历。

## Sqlite中数据存储方式

- 表(table)和索引(Index)都是带顺序访问指针的B+树
- table对应的B+树中，key是rowid，data是这一行其他列数据（sqlite为每一行分配了一个rowid）
- index对应的B+树种，key是需要索引的列，data是rowid

根据索引查找数据时，分两步

1. 根据索引找到rowid（第一次B+树查找）
2. 根据rowid查找其他列的数据（第二次B+树查找）

通过两次B+树查找避免了一次全表扫描。

```
1. 对某一行或某几行添加PRIMARY KEY或UNIQUE约束，那么数据库会自动为这些列创建索引
2. 指定某一列为INTEGER PRIMARY KEY，那么这一列和rowid被指定为同一列。即可以通过rowid来获取，也可以通过列名来获取。
```

### 一个例子

下面是一个数据库中一个表的统计信息，通过[sqlite3_analyzer](https://sqlite.org/sqlanalyze.html)工具得到。  
 ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000347698-1724258368.jpg)￼  
 可以看到表中一共有3651条记录，B树的深度只有2，有33个叶子节点，1个非叶子节点。因此最多只需要2次磁盘IO就可以根据rowid找到一行的数据。

## 利用索引提高查找效率

比如我们有这么一个表  
 ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000317636-1537789799.jpg)￼

1. benchmark  
   查询语句如下

  ```
  SELECT price FROM fruitsforsale WHERE fruit=‘Peach’
  ```

  由于没有索引，因此不得不做一次全表扫描。通过顺序访问指针遍历各个记录(record)，比较fruit这一列和‘peatch’是否一致，如果一致，返回这一行的price列的值。  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000305198-65908804.jpg)￼
2. 对‘fruit’列加索引  
   如下，运行同样的语句，可以根据索引找到目标列对应的rowid为4，然后根据rowid找到对应行，从而选出price。通过两次B+树查找避免了全表查找。这也是最简单的情况   
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000306776-1481600468.jpg)￼
3. 多条索引命中  
   建立索引时，不要求索引是uique的，即索引表中的key可以是一样的。  
   如下图，索引表中有`orange`两条记录，找到第一条记录时，根据顺序访问指针可以轻易找到下一条索引，避免另一次B+树查找。（rowid=1和rowid=23可能位于两个不同的叶子节点中）  
   即这个查找索引的过程，可以通过一次B+树查和一次next操作完成，而next操作是很快的。  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000311698-940240936.jpg)￼
4. 利用索引加快搜索和排序  
   在大多情况下，我们需要同时进行查找和排序操作，这时如果建立适当的索引，可以提高查找效率。  
   比如下面表中对fruit和state两列做了索引，运行下面的sql语句时，就不需要进行排序操作了，因为索引表是带有顺序的。

  ```
  SELECT price FROM fruitforsale WHERE fruit='Orange' ORDER BY state
  ```

  ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000314698-1558154758.jpg)￼

## 解释引言中问题

在sqlite中有一个命令叫做`explain query plan`，可以查看sqlite是如何执行查找操作的。下面的数据库语句不是引言中的查询语句，原理一样

- 37s的操作（没有用索引）  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000311995-444742031.jpg)￼
- 0.2s的操作（用了索引）  
   ![](https://images2015.cnblogs.com/blog/669116/201612/669116-20161223000311011-808027072.jpg)￼

注意detail列。不用索引时，使用的是“SCAN”这个词，即全表扫描。使用索引时，使用的是“SEARCH”这个词。  
 对于一个41G的表来说，进行全表扫描的代价显然是很大的。

## 参考链接

1. [浅谈算法和数据结构: 十 平衡查找树之B树](http://www.cnblogs.com/yangecnu/p/Introduce-B-Tree-and-B-Plus-Tree.html)
2. [MySQL索引背后的数据结构及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)
3. [Query Planning(这篇是sqlite关于索引的文档)](https://www.sqlite.org/queryplanner.html)
4. [EXPLAIN QUERY PLAN](https://www.sqlite.org/eqp.html)
5. [MySQL单表百万数据记录分页性能优化](http://www.cnblogs.com/lyroge/p/3837886.html)

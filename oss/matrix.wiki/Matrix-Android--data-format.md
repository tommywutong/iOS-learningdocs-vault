## 通用字段
1. type:类型，用于区分同一个tag不同类型的上报
2. tag: 该上报对应的tag
3. stack:该上报对应的堆栈
4. process:该上报对应的进程名
5. time:issue 发生的时间

## 耗时上报
### trace(包括启动、慢函数和 FPS 三种)

共同字段：

1. machine: 区分设备好坏的字段
2. process: 进程

#### 启动

1. tag: Trace_StartUp
2. scene: 对应的场景
3. application_create：应用启动的耗时
4. first_activity_create：activity 启动耗时
5. stage_between_app_and_activity: 介于应用和 activity 两者之间的耗时
6. splash_activity_duration，欢迎页耗时
7. startup_duration 启动总耗时
8. is_warm_start_up: 是否是软启动,值范围: true 和 false
9. application_create_scene：启动的场景
   * 100 （activity拉起的）
   * 114（service拉起的）
   * 113 （receiver拉起的）
   * -100 （未知，比如contentprovider）

```
{"machine":4,"application_create":415,"first_activity_create":240,"stage_between_app_and_activity":0,"scene":"com.tencent.mm.app.WeChatSplashActivity","is_warm_start_up":false,"tag":"Trace_StartUp","process":"com.tencent.mm","time":1528278018147}
```

#### 慢函数

对于stack需要通过method_mapping文件解析堆栈，mapping文件在上传安装包的时候需要一起上传。 特殊字段如下：

1. tag: Trace_EvilMethod

2. detail，具体的耗时场景  
   a. NORMAL, 普通慢函数场景  
   b. ENTER, Activity进入场景  
   c. ANR, anr超时场景  
   d. FULL, 满buffer场景
   e. STARTUP, 启动耗时场景

3. cost: 耗时

4. stack: 堆栈

5. stackKey: 客户端提取的 key，用来标识 issue 的唯一性

如果 detail == ENTER, 会增加viewInfo字段, 包括一下三个属性：

1. viewDeep: view 的深度，是个整数
2. viewCount: view 的数量，是个整数
3. activity: activity 的 name

如果 detail == STARTUP, 会增加subType 字段，默认值-1

* subType=1，代表application初始化过程的堆栈
* subType=2，代表启动第一个界面初始化过程的堆栈

```json
{"machine":2015,"detail":"ENTER","cost":3205,"viewInfo":{"viewDeep":10,"viewCount":6,"activity":"TestFpsActivity"},"stack":"3,195,1,10\n1,33,1,58\n2,206,1,21\n3,161,1,16\n4,180,1,16\n5,169,1,16\n6,96,1,10\n7,98,1,10\n4,183,2,5\n5,211,6,0\n0,30,1,56\n","stackKey":"0,30,1,56\n","tag":"Trace_EvilMethod","process":"sample.tencent.matrix"}
```

#### 帧率

帧率这边需要统计整体帧率，已经按场景统计帧率情况

1. tag: Trace_FPS
2. scene：帧率对应的场景
3. dropLevel：衡量帧率掉帧的水平
4. dropSum：总共掉帧的总时长
5. fps: 帧率    

```
{"machine":2015,"scene":"sample.tencent.matrix.trace.TestFpsActivity","dropLevel":{"DROPPED_HIGH":4,"DROPPED_MIDDLE":12,"DROPPED_NORMAL":18,"DROPPED_BEST":113},"dropSum":{"DROPPED_HIGH":60,"DROPPED_MIDDLE":96,"DROPPED_NORMAL":51,"DROPPED_BEST":6},"fps":24.476625442504883,"tag":"Trace_FPS","process":"sample.tencent.matrix"}
```

## 内存泄漏上报
内存泄漏的具体信息如下：

1. tag: memory
2. resultZipPath:对应资源泄漏的hrpof文件，已经过裁剪。 
3. activity：泄漏的Activity名称

### 事例
内存泄漏这里我们通过文件上传方式，事例如下：

	{"resultZipPath":"\/storage\/emulated\/0\/Android\/data\/com.tencent.mm\/cache\/matrix_resource\/dump_result_17400_20170713183615.zip","activity":"com.tencent.mm.plugin.setting.ui.setting.SettingsUI","tag":"memory","process":"com.tencent.mm"}

这里有两部分的异常：

1. duplicated_bitmap: 内存出现重复的bitmap对象以及堆栈，这里会直接生成重复图片文件
2. leaked_activities：泄漏的Activity以及堆栈

考虑到性能，除了上传 Hprof 文件，我们还有轻量级的上报(不需要 dump Hprof 文件)，走数据上报通道，所以除了需要解析 Hprof 文件，还需要从数据通道那里解析数据：

```
{"activity":"com.tencent.mm.plugin.setting.ui.setting.SettingsUI","tag":"memory","process":"com.tencent.mm"}
```

## IO上报
IO 当前存在四种类型的上报,的具体信息如下：

1. tag: io

2. type，耗时这边的类型有两种
  a. MAIN_THREAD_IO=1, 在主线程IO超过200ms
  b. BUFFER_TOO_SMALL=2, 重复读取同一个文件,同一个堆栈超过3次
  c. REPEAT_IO=3, 读写文件的buffer过小，即小于4k
  d. CLOSE_LEAK=4, 文件泄漏

3. path: 文件的路径

4. size: 文件的大小

5. cost: 读写的耗时

6. stack: 读写的堆栈

7. op: 读写的次数

8. buffer: 读写所用的buffer大小，要求大于4k

9. thread: 线程名

10. opType: 1为读，2为写

11. opSize: 读写的总大小

12. repeat: 

    a. REPEAT_IO : 重复的次数

    b. Main_IO：1 - 单次操作 2 - 连续读写 3 -2种行为

### IO事例

IO的字段基本一样，下面是重复IO的一个事例。

	{"path":"\/data\/user\/0\/com.tencent.mm\/MicroMsg\/MM_stepcounter.cfg","size":496,"op":60,"buffer":289,"cost":7,"opType":"r","opSize":496,"thread":"MM_Thread_Pool_Free_Handler_Thread#3#initThread","stack":"java.io.FileInputStream.<init>(FileInputStream.java:76)\ncom.tencent.mm.storage.ConfigFileStorage.openCfg(ConfigFileStorage.java:78)\ncom.tencent.mm.storage.ConfigFileStorage.<init>(ConfigFileStorage.java:30)\ncom.tencent.mm.plugin.sport.model.SportFileStorage.<init>(SportFileStorage.java:12)\ncom.tencent.mm.plugin.sport.model.SportFileStorageLogic.create(SportFileStorageLogic.java:21)\ncom.tencent.mm.plugin.sport.PluginSport.execute(PluginSport.java:44)\ncom.tencent.mm.kernel.boot.Boot.executeTask(Boot.java:111)\ncom.tencent.mm.kernel.boot.Boot$1.call(Boot.java:71)\n","tag":"io","type":3,"process":"com.tencent.mm"}

资源泄漏的上报会不太一样，具体如下：

	"stack":"dalvik.system.CloseGuard.open(CloseGuard.java:180)\njava.io.RandomAccessFile.<init>(RandomAccessFile.java:127)\ncom.tencent.smtt.utils.DataReader.<init>(Unknown Source)\ncom.tencent.smtt.utils.DataReader.<init>(Unknown Source)\ncom.tencent.smtt.sdk.OatHelper.getOatCommand(Unknown Source)\ncom.tencent.smtt.sdk.TbsInstaller.doDexoatForArtVm(Unknown Source)\ncom.tencent.smtt.sdk.TbsInstaller.doDexoptOrDexoat(Unknown Source)\ncom.tencent.smtt.sdk.TbsInstaller.installTbsCoreInThread(Unknown Source)\n","tag":"io","type":4,"process":"com.tencent.mm:sandbox"}

## SQLiteLint上报

具体信息如下：

1. tag: SQLiteLint

2. id: 用来标识 issue 类别的唯一性，例如：多个用户的 id 一样说明是同一个 issue

3. type

   ```c++
   typedef enum {
       kExplainQueryScanTable = 1, // 全表扫描，遍历数据表查找结果集，复杂度O(n)
       kExplainQueryUseTempTree, // 不必要的临时建树排序， 可用索引优化
       kExplainQueryTipsForLargerIndex, // 不足够的索引组合
       kAvoidAutoIncrement, // 使用了Autoincrement, 应避免使用
       kAvoidSelectAllChecker, // 使用了select *, 如非必要只需查询自己需要的列
       kWithoutRowIdBetter,	// 建议使用without rowid特性
       kPreparedStatementBetter,	// 建议使用prepared statement
       kRedundantIndex,	// 发现冗余索引
   } IssueType;
   ```

4. dbPath: 数据库路径

5. level:

   ```cpp
   typedef enum {
       kPass = 0,
       kTips,
       kSuggestion,
       kWarning,
       kError,
   } IssueLevel;
   ```

6. table: 表名

7. sql: 相关sql语句

8. desc: 问题描述

9. detail:  问题更详细的描述，如查询计划。

10. advice: 优化建议

11. createTime: 发现 issue 的时间

12. stack: 该上报对应的堆栈

13. isInMainThread: 是否在主线程

14. sqlTimeCost: sql 执行耗时，单位 ms.  __注意：__ 只有 kExplainQueryScanTable kExplainQueryUseTempTree kExplainQueryTipsForLargerIndex kAvoidSelectAllChecker 这几种此字段才有效

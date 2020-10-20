case 1:
  使用同一个bag中不同topic进行共同运算or逻辑判断


case 2:
  使用同一个msg下的不同data进行共同运算or逻辑判断
  用available判断数据取0或者直接保存
  用data.x和data.y计算新的值保留下来
  
case 3:
  不同bag中进行共同运算
  两个bag同步时间戳



## Feature
  * 查找string literal parsing
  * 多线程agent存储
  * declaritive looping design pattern
  * prompt

## problem
  * 多个bag如何同时读：
    * 不同时读，只能单独去读（限制很大）
      * 检查是否为同一个包，如果不是就报错
      * 但是已经满足了我们的预期
    * 同时读，设置两个模式，按时间顺序读，还有同时开始按时间读
      * 这就必须用多线程，并且为了保证先后顺序需要设置锁
      * 或者不用多线程，但是在loop中也要有类似的锁逻辑
      * 这个逻辑不交给用户处理

    * 第二个情况是兼容第一个情况的
      * 每个frame meta的定义确定了，就是当前时间戳拿到的所有缓存值 
      * 每次读到新的msg，就会触发对应监听的frame meta一次

  * 多个topic/bag同时读的应用场景
    * 其实仔细想想，如果用户没有规定两个不同步的数据序列间的运算的逻辑和先后顺序等，本身就是个伪命题
    * 不需要用户规定逻辑的场景可能就是filter的情况了，这个对于不同步时间序列是有意义的

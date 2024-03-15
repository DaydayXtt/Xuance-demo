# Xuance-demo
关于在WINDOWS系统下调试通过强化学习测试包——玄策
https://xuance.readthedocs.io/zh/latest/documents/usage/installation.html
# conda安装（Pytorch版本）
    conda create -n xuance_env python=3.7
    conda activate xuance_env
    pip install xuance[torch]
## 验证
虚拟环境下输入：

    python
    import xuance
没有异常则表明OK
## ERROR:
![image](https://github.com/DaydayXtt/Xuance-demo/blob/main/user-manual/error-when-import.png)

原因：Windows缺少MPI，需要安装（2个文件，一切默认）

https://www.microsoft.com/en-us/download/details.aspx?id=105289

# 更换gpu版本
xuance默认pytorch为cpu版本，需要更换为GPU版本。虚拟环境下卸载pytorch：

    pip uninstall torch
然后进入官网重装cuda版本的torch(1.13.0/1皆可)，注意CUDA版本。
https://blog.csdn.net/qq_45973897/article/details/130259533
        
    # CUDA 11.6
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia

## 更换玄策配置文件
找到 "~\Anaconda3\envs\xuance\Lib\site-packages\xuance\configs" 下的basic.yaml文件，修改：
    
    device: "cuda:0"

# run and test
参照：https://xuance.readthedocs.io/zh/latest/documents/usage/installation.html

## 后续...
测试结果可视化演示
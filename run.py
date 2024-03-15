import xuance

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    runner = xuance.get_runner(method='td3',
                               env='box2d',
                               env_id='BipedalWalker-v3',
                               is_test=False)
    runner.run()

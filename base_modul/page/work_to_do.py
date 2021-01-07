from base_page import basepage
class worktode(basepage):
    #定位分离
    #定位弹窗
    def worktable(self):
        return self.css('div.text-center .el-checkbox__inner')
    def clikok(self):
        return self.css('button.declar-checked')

    #操作元素动作分离
    #点击弹窗
    def worktable_do(self):
        self.worktable().click()
    def clik(self):
        self.clikok().click()






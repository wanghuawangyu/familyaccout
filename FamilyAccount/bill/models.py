from django.db import models

# Create your models here.
class Family(models.Model):
    family_id=models.AutoField(primary_key=True,verbose_name='家庭id')
    familyName=models.CharField(max_length=64,null=False,verbose_name='家庭昵称')
    addDate=models.DateTimeField(auto_now_add=True,verbose_name='创建日期')
    def __str__(self):
        str=self.familyName
        return str
    class Meta:
        # db_table = 'family'
        verbose_name = '家庭'
        verbose_name_plural =verbose_name
        ordering = ['family_id']

class User(models.Model):
    user_id=models.AutoField(primary_key=True,verbose_name='用户id')
    userName=models.CharField(max_length=64,verbose_name='用户姓名')
    userTel=models.CharField(max_length=11,verbose_name='用户电话')
    userEmail=models.EmailField(verbose_name='用户邮箱')
    haveFamily=models.BooleanField(default=False,verbose_name='是否加入家庭')
    isFamilyHead=models.BooleanField(default=False,verbose_name='是否家长')
    isActive=models.BooleanField(default=False,verbose_name='用户账号是否激活')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    family_id=models.ForeignKey(Family,null=True,verbose_name='用户的家庭') #外键，关联家庭，多个用户属于一个家庭
    familyMarkName=models.CharField(max_length=64,null=True,verbose_name='用户在家庭的简称')
    familyOrderNumber=models.IntegerField(default=0,verbose_name='用户在家庭中显示顺序')
    def __str__(self):
        str=self.userName
        return str
    class Meta:
        # db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural =verbose_name
        ordering = ['user_id']

class Trade(models.Model):
    trade_id=models.AutoField(primary_key=True,verbose_name='账目类型id')
    tradeName=models.CharField(max_length=64,verbose_name='账目类型')
    tradeDescrition=models.CharField(max_length=64,null=True,verbose_name='账目说明')
    tradeOrderNumber=models.IntegerField(default=0,verbose_name='账目显示顺序号')
    tradeOrderMark=models.CharField(max_length=64,verbose_name='账目备注')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    tradeTypeToUser=models.ForeignKey(User,verbose_name='账目所属用户') #外键，多个账目属于一个用户
    def __str__(self):
        str=self.tradeName
        return str
    class Meta:
        # db_table = 'trade'
        verbose_name = '账目'
        verbose_name_plural =verbose_name
        ordering = ['trade_id']

class Card(models.Model):
    card_id=models.AutoField(primary_key=True,verbose_name='卡片id')
    cardName=models.CharField(max_length=64,verbose_name='卡片名称')
    cardDescrition=models.CharField(max_length=64,null=True,verbose_name='卡片描述')
    cardType=models.CharField(max_length=10,verbose_name='卡片类型')
    cardNumber=models.CharField(max_length=20,verbose_name='卡片号码')
    cardFixedCredits=models.IntegerField(default=0,verbose_name='卡片固定额度')
    cardStartAmount=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='卡片初始金额')
    cardBillday=models.CharField(max_length=10,verbose_name='卡片账单日')
    cardRepaymentDay=models.CharField(max_length=10,verbose_name='卡片最后还款日')
    isCardActive=models.BooleanField(default=False,verbose_name='卡片是否激活')
    isCardCount=models.BooleanField(default=False,verbose_name='卡片是否汇总')
    cardOrderNumber=models.IntegerField(default=0,verbose_name='卡片显示顺序号')
    cardRemark=models.CharField(max_length=128,verbose_name='卡片备注')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    cardToUser=models.ForeignKey(User,verbose_name='卡片所属用户') #外键，多张卡属于一个用户
    def __str__(self):
        str=self.cardName
        return str
    class Meta:
        # db_table = 'card'
        verbose_name = '银行账户'
        verbose_name_plural =verbose_name
        ordering = ['card_id']

class Subject(models.Model):
    subject_id=models.AutoField(primary_key=True,verbose_name='科目id')
    subjectName=models.CharField(max_length=64,verbose_name='科目名称')
    subjectDescrition=models.CharField(max_length=128,null=True,verbose_name='科目描述')
    isSubjectActive=models.BooleanField(default=False,verbose_name='科目是否启用')
    isSubjectCount=models.BooleanField(default=False,verbose_name='科目是否汇总')
    subjectOrderNumber=models.IntegerField(default=0,verbose_name='科目显示顺序号')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    subjectToUser=models.ForeignKey(User,verbose_name='科目所属用户') #外键，多科目属于一个用户
    def __str__(self):
        str=self.subjectName
        return str
    class Meta:
        # db_table = 'subject'
        verbose_name = '记账科目'
        verbose_name_plural =verbose_name
        ordering = ['subject_id']

class Detail(models.Model):
    detail_id=models.AutoField(primary_key=True,verbose_name='流水id')
    detailDate=models.DateTimeField(auto_now_add=True,verbose_name='流水创建日期')
    tradeDate=models.DateTimeField(auto_now_add=True,verbose_name='交易发生日期')
    tradeNumber=models.BigIntegerField(verbose_name='交易编号')
    detailDescription=models.CharField(max_length=128,null=True,verbose_name='交易描述')
    detailAmount=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='交易金额')
    detailNo=models.SmallIntegerField(default=1,verbose_name='记录数量')
    installment=models.BooleanField(default=False,verbose_name='是否分期')
    isCardOtherCredits=models.BooleanField(default=False,verbose_name='是否额外授信额度')
    isDetailActive=models.BooleanField(default=False,verbose_name='账单是否发生')

    detailToUser=models.OneToOneField(User,verbose_name='交易用户') #一对一 一条流水对应一个用户
    detailToTradeType=models.OneToOneField(Trade,verbose_name='交易账目') #一对一 一条流水对应一个交易类型
    detailToCard=models.OneToOneField(Card,verbose_name='交易卡片') #一对一 一条流水对应一个交易卡片
    detailToSubject=models.OneToOneField(Subject,verbose_name='交易记账科目') #一对一 一条流水对应一个记账科目

    class Meta:
        # db_table = 'detail'
        verbose_name = '交易流水'
        verbose_name_plural =verbose_name
        ordering = ['-detail_id']

class Bill(models.Model):
    bill_id=models.AutoField(primary_key=True,verbose_name='账单id')
    billDate=models.DateField(auto_now_add=True,verbose_name='账单日期')
    billAmount=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='账单金额')
    billRepaymentDate=models.DateField(null=False,verbose_name='最后还款日期')
    isRepayment=models.BooleanField(default=False,verbose_name='是否还清')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='记录创建日期')

    billToUser=models.OneToOneField(User,verbose_name='账单用户') #一对一 一条账单对应一个用户
    billToCard=models.OneToOneField(Card,verbose_name='账单卡片') #一对一 一条账单对应一张卡片
    class Meta:
        # db_table = 'bill'
        verbose_name = '账单记录'
        verbose_name_plural =verbose_name
        ordering = ['-billDate']

class Installment(models.Model):
    installment_id=models.AutoField(primary_key=True,verbose_name='贷款记录id')
    installmentNumber=models.PositiveIntegerField(verbose_name='贷款编号')
    installmentDescription=models.CharField(max_length=128,null=True,verbose_name='贷款描述')
    installmentDate=models.DateField(auto_now_add=True,verbose_name='贷款日期')
    installmentStartDate=models.DateField(auto_now_add=True,verbose_name='贷款账目开始日期')
    installmentEndDate=models.DateField(auto_now_add=True,verbose_name='贷款账目结束日期')
    addDate = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    installmentMonthNumner=models.SmallIntegerField(default=12,verbose_name='贷款期数')
    isAllowPrepayment=models.BooleanField(default=False,verbose_name='是否可以提前还款')
    prepaymentRate=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='提前还款手续费率')
    repaymentMethod=models.CharField(max_length=20,verbose_name='还款方式')
    interestRatePerYear=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='年利率')
    installmentAmount=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='贷款金额')
    isPayNextInterest=models.BooleanField(default=False,verbose_name='提前还款是否支付剩余手续费')

    installmentToUser=models.OneToOneField(User,verbose_name='贷款用户') #一对一 一条分期记录对应一个用户
    InstallmentToCard=models.OneToOneField(Card,verbose_name='贷款所属卡片') #一对一 一条分期记录对应一张卡片
    class Meta:
        # db_table = 'installment'
        verbose_name = '贷款记录'
        verbose_name_plural =verbose_name
        ordering = ['-installmentDate']

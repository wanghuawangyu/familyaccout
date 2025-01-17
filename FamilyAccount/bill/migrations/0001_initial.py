# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-24 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False, verbose_name='账单id')),
                ('billDate', models.DateField(auto_now_add=True, verbose_name='账单日期')),
                ('billAmount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账单金额')),
                ('billRepaymentDate', models.DateField(verbose_name='最后还款日期')),
                ('isRepayment', models.BooleanField(default=False, verbose_name='是否还清')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='记录创建日期')),
            ],
            options={
                'verbose_name': '账单记录',
                'verbose_name_plural': '账单记录',
                'ordering': ['-billDate'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False, verbose_name='卡片id')),
                ('cardName', models.CharField(max_length=64, verbose_name='卡片名称')),
                ('cardDescrition', models.CharField(default=None, max_length=64, verbose_name='卡片描述')),
                ('cardType', models.CharField(max_length=10, verbose_name='卡片类型')),
                ('cardNumber', models.CharField(max_length=20, verbose_name='卡片号码')),
                ('cardFixedCredits', models.IntegerField(default=0, verbose_name='卡片固定额度')),
                ('cardStartAmount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='卡片初始金额')),
                ('cardBillday', models.CharField(max_length=10, verbose_name='卡片账单日')),
                ('cardRepaymentDay', models.CharField(max_length=10, verbose_name='卡片最后还款日')),
                ('isCardActive', models.BooleanField(default=False, verbose_name='卡片是否激活')),
                ('isCardCount', models.BooleanField(default=False, verbose_name='卡片是否汇总')),
                ('cardOrderNumber', models.IntegerField(default=0, verbose_name='卡片显示顺序号')),
                ('cardRemark', models.CharField(max_length=128, verbose_name='卡片备注')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '银行账户',
                'verbose_name_plural': '银行账户',
                'ordering': ['card_id'],
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False, verbose_name='流水id')),
                ('detailDate', models.DateTimeField(auto_now_add=True, verbose_name='流水创建日期')),
                ('tradeDate', models.DateTimeField(auto_now_add=True, verbose_name='交易发生日期')),
                ('tradeNumber', models.PositiveIntegerField(verbose_name='交易编号')),
                ('detailDescription', models.CharField(max_length=128, verbose_name='交易描述')),
                ('detailAmount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='交易金额')),
                ('detailNo', models.SmallIntegerField(default=1, verbose_name='记录数量')),
                ('installment', models.BooleanField(default=False, verbose_name='是否分期')),
                ('isCardOtherCredits', models.BooleanField(default=False, verbose_name='是否额外授信额度')),
                ('isDetailActive', models.BooleanField(default=False, verbose_name='账单是否发生')),
                ('detailToCard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.Card', verbose_name='交易卡片')),
            ],
            options={
                'verbose_name': '交易流水',
                'verbose_name_plural': '交易流水',
                'ordering': ['-detail_id'],
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('family_id', models.AutoField(primary_key=True, serialize=False, verbose_name='家庭id')),
                ('familyName', models.CharField(max_length=64, verbose_name='家庭昵称')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '家庭',
                'verbose_name_plural': '家庭',
                'ordering': ['family_id'],
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('installment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='贷款记录id')),
                ('installmentNumber', models.PositiveIntegerField(verbose_name='贷款编号')),
                ('installmentDescription', models.CharField(default=None, max_length=128, verbose_name='贷款描述')),
                ('installmentDate', models.DateField(auto_now_add=True, verbose_name='贷款日期')),
                ('installmentStartDate', models.DateField(auto_now_add=True, verbose_name='贷款账目开始日期')),
                ('installmentEndDate', models.DateField(auto_now_add=True, verbose_name='贷款账目结束日期')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('installmentMonthNumner', models.SmallIntegerField(default=12, verbose_name='贷款期数')),
                ('isAllowPrepayment', models.BooleanField(default=False, verbose_name='是否可以提前还款')),
                ('prepaymentRate', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='提前还款手续费率')),
                ('repaymentMethod', models.CharField(max_length=20, verbose_name='还款方式')),
                ('interestRatePerYear', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='年利率')),
                ('installmentAmount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='贷款金额')),
                ('isPayNextInterest', models.BooleanField(default=False, verbose_name='提前还款是否支付剩余手续费')),
                ('InstallmentToCard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.Card', verbose_name='贷款所属卡片')),
            ],
            options={
                'verbose_name': '贷款记录',
                'verbose_name_plural': '贷款记录',
                'ordering': ['-installmentDate'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False, verbose_name='科目id')),
                ('subjectName', models.CharField(max_length=64, verbose_name='科目名称')),
                ('subjectDescrition', models.CharField(default=None, max_length=128, verbose_name='科目描述')),
                ('isSubjectActive', models.BooleanField(default=False, verbose_name='科目是否启用')),
                ('isSubjectCount', models.BooleanField(default=False, verbose_name='科目是否汇总')),
                ('subjectOrderNumber', models.IntegerField(default=0, verbose_name='科目显示顺序号')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '记账科目',
                'verbose_name_plural': '记账科目',
                'ordering': ['subject_id'],
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('trade_id', models.AutoField(primary_key=True, serialize=False, verbose_name='账目类型id')),
                ('tradeName', models.CharField(max_length=64, verbose_name='账目类型')),
                ('tradeDescrition', models.CharField(default=None, max_length=64, verbose_name='账目说明')),
                ('tradeOrderNumber', models.IntegerField(default=0, verbose_name='账目显示顺序号')),
                ('tradeOrderMark', models.CharField(max_length=64, verbose_name='账目备注')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '账目',
                'verbose_name_plural': '账目',
                'ordering': ['trade_id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('userName', models.CharField(max_length=64, verbose_name='用户姓名')),
                ('userTel', models.CharField(max_length=11, verbose_name='用户电话')),
                ('userEmail', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('haveFamily', models.BooleanField(default=False, verbose_name='是否加入家庭')),
                ('isFamilyHead', models.BooleanField(default=False, verbose_name='是否家长')),
                ('isActive', models.BooleanField(default=False, verbose_name='用户账号是否激活')),
                ('addDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('familyMarkName', models.CharField(default=None, max_length=64, verbose_name='用户在家庭的简称')),
                ('familyOrderNumber', models.IntegerField(default=0, verbose_name='用户在家庭中显示顺序')),
                ('family_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bill.Family', verbose_name='用户的家庭')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['user_id'],
            },
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeTypeToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='账目所属用户'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subjectToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='科目所属用户'),
        ),
        migrations.AddField(
            model_name='installment',
            name='installmentToUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='贷款用户'),
        ),
        migrations.AddField(
            model_name='detail',
            name='detailToSubject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.Subject', verbose_name='交易记账科目'),
        ),
        migrations.AddField(
            model_name='detail',
            name='detailToTradeType',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.Trade', verbose_name='交易账目'),
        ),
        migrations.AddField(
            model_name='detail',
            name='detailToUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='交易用户'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardToUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='卡片所属用户'),
        ),
        migrations.AddField(
            model_name='bill',
            name='billToCard',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.Card', verbose_name='账单卡片'),
        ),
        migrations.AddField(
            model_name='bill',
            name='billToUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bill.User', verbose_name='账单用户'),
        ),
    ]

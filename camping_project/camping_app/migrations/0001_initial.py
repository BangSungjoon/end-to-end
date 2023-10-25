# Generated by Django 4.2.6 on 2023-10-25 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_no', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateTimeField()),
                ('stay_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampInfo',
            fields=[
                ('camp_no', models.AutoField(primary_key=True, serialize=False)),
                ('camp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_s_tt', models.CharField(blank=True, max_length=200, null=True)),
                ('camp_tag_li', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_address', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_call', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_environment', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_type', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_period', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_day', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_pagelink', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_book', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_itd', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'camp_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampMemeberInfo',
            fields=[
                ('camp_no', models.AutoField(primary_key=True, serialize=False)),
                ('camp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_s_tt', models.CharField(blank=True, max_length=200, null=True)),
                ('camp_tag_li', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_address', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_call', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_environment', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_type', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_period', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_ope_day', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_pagelink', models.CharField(blank=True, max_length=500, null=True)),
                ('camp_book', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_itd', models.TextField(blank=True, null=True)),
                ('approve', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'camp_memeber_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampReview',
            fields=[
                ('review_no', models.AutoField(primary_key=True, serialize=False)),
                ('rev_title', models.CharField(blank=True, max_length=100, null=True)),
                ('rev_content', models.TextField(blank=True, null=True)),
                ('rev_date', models.DateTimeField()),
                ('rev_rate', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'camp_review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('camp_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'favorite_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InqReply',
            fields=[
                ('rep_no', models.IntegerField(primary_key=True, serialize=False)),
                ('rep_content', models.CharField(max_length=500)),
                ('rep_date', models.DateField(blank=True, null=True)),
                ('inq_no', models.IntegerField()),
            ],
            options={
                'db_table': 'inq_reply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInquire',
            fields=[
                ('inq_no', models.AutoField(primary_key=True, serialize=False)),
                ('inq_title', models.CharField(max_length=500)),
                ('inq_content', models.CharField(max_length=500)),
                ('inq_date', models.DateField(blank=True, null=True)),
                ('rep_status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_inquire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersAppUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('user_name', models.CharField(max_length=30)),
                ('user_age', models.IntegerField(blank=True, null=True)),
                ('user_gender', models.IntegerField(blank=True, null=True)),
                ('user_tel', models.CharField(max_length=20)),
                ('user_address', models.CharField(blank=True, max_length=200, null=True)),
                ('user_subscribe_sms', models.IntegerField()),
                ('user_subscribe_email', models.IntegerField()),
            ],
            options={
                'db_table': 'users_app_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersAppUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_app_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersAppUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_app_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampFacInfo',
            fields=[
                ('camp_no', models.OneToOneField(db_column='camp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='camping_app.campinfo')),
                ('camp_main_fac', models.CharField(blank=True, max_length=100, null=True)),
                ('camp_etc_info', models.CharField(blank=True, max_length=45, null=True)),
                ('camp_brazier', models.CharField(blank=True, max_length=10, null=True)),
                ('camp_safe_fac', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'camp_fac_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampTypePrice',
            fields=[
                ('camp_no', models.OneToOneField(db_column='camp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='camping_app.campinfo')),
                ('camp_normal_off_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_normal_off_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_normal_peak_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_normal_peak_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_auto_off_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_auto_off_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_auto_peak_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_auto_peak_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_glam_off_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_glam_off_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_glam_peak_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_glam_peak_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_crv_off_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_crv_off_season_price_we', models.IntegerField(blank=True, null=True)),
                ('camp_crv_peak_season_price_wd', models.IntegerField(blank=True, null=True)),
                ('camp_crv_peak_season_price_we', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'camp_type_price',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampUtility',
            fields=[
                ('camp_no', models.OneToOneField(db_column='camp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='camping_app.campinfo')),
                ('electric', models.IntegerField(blank=True, null=True)),
                ('wifi', models.IntegerField(blank=True, null=True)),
                ('firewood', models.IntegerField(blank=True, null=True)),
                ('warm_water', models.IntegerField(blank=True, null=True)),
                ('walking_load', models.IntegerField(blank=True, null=True)),
                ('sports_ground', models.IntegerField(blank=True, null=True)),
                ('market', models.IntegerField(blank=True, null=True)),
                ('water_playground', models.IntegerField(blank=True, null=True)),
                ('athletic_fac', models.IntegerField(blank=True, null=True)),
                ('adv_ground', models.IntegerField(blank=True, null=True)),
                ('trampoline', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'camp_utility',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImageLink',
            fields=[
                ('camp_no', models.OneToOneField(db_column='camp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='camping_app.campinfo')),
                ('main_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('col1_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('col2_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('col3_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('last1_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('last2_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('last3_img_link', models.CharField(blank=True, max_length=150, null=True)),
                ('last4_img_link', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'image_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersAppCompanyuser',
            fields=[
                ('user_ptr', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='camping_app.usersappuser')),
                ('company_name', models.CharField(max_length=30)),
                ('company_tel', models.CharField(max_length=20)),
                ('company_address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'users_app_companyuser',
                'managed': False,
            },
        ),
    ]

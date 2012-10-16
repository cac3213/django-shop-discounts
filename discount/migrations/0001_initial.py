# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DiscountBase'
        db.create_table('discount_discountbase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_discount.discountbase_set', null=True, to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('valid_until', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('num_uses', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('discount', ['DiscountBase'])

        # Adding model 'CartDiscountCode'
        db.create_table('discount_cartdiscountcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Cart'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('discount', ['CartDiscountCode'])

        # Adding model 'PercentDiscount'
        db.create_table('discount_percentdiscount', (
            ('discountbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['discount.DiscountBase'], unique=True, primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('discount', ['PercentDiscount'])

        # Adding model 'AbsoluteDiscount'
        db.create_table('discount_absolutediscount', (
            ('discountbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['discount.DiscountBase'], unique=True, primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('discount', ['AbsoluteDiscount'])

        # Adding model 'CartItemPercentDiscount'
        db.create_table('discount_cartitempercentdiscount', (
            ('discountbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['discount.DiscountBase'], unique=True, primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('discount', ['CartItemPercentDiscount'])

        # Adding model 'CartItemAbsoluteDiscount'
        db.create_table('discount_cartitemabsolutediscount', (
            ('discountbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['discount.DiscountBase'], unique=True, primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('discount', ['CartItemAbsoluteDiscount'])


    def backwards(self, orm):
        # Deleting model 'DiscountBase'
        db.delete_table('discount_discountbase')

        # Deleting model 'CartDiscountCode'
        db.delete_table('discount_cartdiscountcode')

        # Deleting model 'PercentDiscount'
        db.delete_table('discount_percentdiscount')

        # Deleting model 'AbsoluteDiscount'
        db.delete_table('discount_absolutediscount')

        # Deleting model 'CartItemPercentDiscount'
        db.delete_table('discount_cartitempercentdiscount')

        # Deleting model 'CartItemAbsoluteDiscount'
        db.delete_table('discount_cartitemabsolutediscount')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'discount.absolutediscount': {
            'Meta': {'object_name': 'AbsoluteDiscount', '_ormbases': ['discount.DiscountBase']},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'discountbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['discount.DiscountBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'discount.cartdiscountcode': {
            'Meta': {'object_name': 'CartDiscountCode'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Cart']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'discount.cartitemabsolutediscount': {
            'Meta': {'object_name': 'CartItemAbsoluteDiscount', '_ormbases': ['discount.DiscountBase']},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'discountbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['discount.DiscountBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'discount.cartitempercentdiscount': {
            'Meta': {'object_name': 'CartItemPercentDiscount', '_ormbases': ['discount.DiscountBase']},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'discountbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['discount.DiscountBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'discount.discountbase': {
            'Meta': {'object_name': 'DiscountBase'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_uses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_discount.discountbase_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'discount.percentdiscount': {
            'Meta': {'object_name': 'PercentDiscount', '_ormbases': ['discount.DiscountBase']},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'discountbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['discount.DiscountBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['discount']
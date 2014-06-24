# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuItem.language'
        db.add_column(u'treenav_menuitem', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=255),
                      keep_default=False)

        # Adding field 'MenuItem.is_group'
        db.add_column(u'treenav_menuitem', 'is_group',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'MenuItem.parent'
        db.alter_column(u'treenav_menuitem', 'parent_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['treenav.MenuItem']))

        # Changing field 'MenuItem.href'
        db.alter_column(u'treenav_menuitem', 'href', self.gf('django.db.models.fields.CharField')(max_length=2048))

        # Changing field 'MenuItem.link'
        db.alter_column(u'treenav_menuitem', 'link', self.gf('django.db.models.fields.CharField')(max_length=2048))

    def backwards(self, orm):
        # Deleting field 'MenuItem.language'
        db.delete_column(u'treenav_menuitem', 'language')

        # Deleting field 'MenuItem.is_group'
        db.delete_column(u'treenav_menuitem', 'is_group')


        # Changing field 'MenuItem.parent'
        db.alter_column(u'treenav_menuitem', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['treenav.MenuItem']))

        # Changing field 'MenuItem.href'
        db.alter_column(u'treenav_menuitem', 'href', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'MenuItem.link'
        db.alter_column(u'treenav_menuitem', 'link', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'treenav.menuitem': {
            'Meta': {'ordering': "('lft', 'tree_id')", 'object_name': 'MenuItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '255'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['treenav.MenuItem']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['treenav']
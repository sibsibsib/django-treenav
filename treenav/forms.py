from django import forms
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core.validators import URLValidator

import autocomplete_light
from treenav.models import MenuItem
from mptt.forms import TreeNodeChoiceField, MPTTAdminForm


class MenuItemFormMixin(object):

    def clean_link(self):
        link = self.cleaned_data['link'] or ''
        # It could be a fully-qualified URL -- try that first b/c reverse()
        # chokes on "http://"
        if any([link.startswith(s) for s in ('http://', 'https://')]):
            URLValidator()(link)
        elif link and not any([link.startswith(s) for s in ('^', '/')]):
            # Not a regex or site-root-relative absolute path -- see if it's a
            # named URL or view
            try:
                reverse(link)
            except NoReverseMatch:
                raise forms.ValidationError('Please supply a valid URL, URL '
                                            'name, or regular expression.')
        return self.cleaned_data['link']

    def clean(self):
        super(MenuItemFormMixin, self).clean()

        if 'is_enabled' in self.cleaned_data and \
          self.cleaned_data['is_enabled'] and \
          'link' in self.cleaned_data and \
          self.cleaned_data['link'].startswith('^'):
            raise forms.ValidationError('Menu items with regular expression '
                                        'URLs must be disabled.')
        return self.cleaned_data


class MenuItemForm(MenuItemFormMixin, autocomplete_light.GenericModelForm, MPTTAdminForm):

    content_object = autocomplete_light.GenericModelChoiceField(
        label='linked object',
        required=False,
        widget=autocomplete_light.ChoiceWidget(
            autocomplete='NavigationItems',
            autocomplete_js_attributes={'minimum_characters': 0},
            attrs={'size': '40'},
        ),
    )

    class Meta:
        model = MenuItem


class MenuItemInlineForm(MenuItemFormMixin, autocomplete_light.GenericModelForm, forms.ModelForm):

    content_object = autocomplete_light.GenericModelChoiceField(
        label='linked object',
        required=False,
        widget=autocomplete_light.ChoiceWidget(
            autocomplete='NavigationItems',
            autocomplete_js_attributes={'minimum_characters': 0},
            attrs={'size': '40'},
        ),
    )

    class Meta:
        model = MenuItem


class GenericInlineMenuItemForm(forms.ModelForm):
    parent = TreeNodeChoiceField(
        queryset=MenuItem.tree.all(),
        required=False
    )

    class Meta:
        model = MenuItem
        fields = ('parent', 'label', 'slug', 'order', 'is_enabled')

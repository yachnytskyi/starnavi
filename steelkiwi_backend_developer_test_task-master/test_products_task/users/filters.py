from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class ActivityUserListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('User\'s activity')

    # Parameter for the filter that will be used in the URL query.
    # parameter_name = 'user_activity'
    parameter_name = User.ACTIVITY_PARAM

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return User.ACTIVITY_OPTIONS

    def queryset(self, request, queryset):
        raise NotImplementedError()

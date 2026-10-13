"""
Custom libraries.exceptions definitions
"""


class ConfigurationMissingException(Exception):
    """
    Raise this exception when the configuration is none or empty
    """
    pass


class ConfigurationException(Exception):
    """
    Raise this exception when the configuration is malformed or contains a misconfiguration
    """
    pass


"""
Custom SSLA related exceptions definitions.
May concern metrics, slo or capabilities.
"""


class SSLAException(Exception):
    """
    Raise this exception when the SSLA contains a high-level issue
    """
    pass


class SSLAAlreadyExistsException(SSLAException):
    """
    Raise this exception when an SSLA is already stored for the targeted service
    """
    pass


class SSLAValidationException(SSLAException):
    """
    Raise this exception when the SSLA does not comply with the XML Schema
    """
    pass


class SSLAFormatException(SSLAException):
    """
    Raise this exception when the SSLA contains the wrong format
    """
    pass


class SSLAServiceDescriptionException(SSLAException):
    """
    Raise this exception when the SSLA contains an issue related to Service Description
    """
    pass


class SSLACapabilityException(SSLAException):
    """
    Raise this exception when the SSLA contains an issue related to SLOs
    """
    pass


class SSLASLOException(SSLAException):
    """
    Raise this exception when the SSLA contains an issue related to SLOs
    """
    pass


class SSLAMetricsException(SSLAException):
    """
    Raise this exception when the SSLA contains an issue related to metrics
    """
    pass


class SSLANotFound(SSLAException):
    """
    Raise this exception when the SSLA contains an issue related to metrics
    """
    pass

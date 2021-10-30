import logging
import math

# basicConfig, getLogger

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"  # Including more info, we use asctime, levelname, message

logging.basicConfig(filename="E:\\Computer Science\\Python\\Logging\\Pythonlog.log", level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')

logger = logging.getLogger()

# NOTSET=0, DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50

logger.info("Our first message.")
print(logger.level)

logger.info("Our second message.")


def quadratic_formula(a, b, c, ):
    """ solution to ax^2 + bx + c =0"""
    logger.info("quadratic_formula({0},{1},{2})".format(a, b, c))

    # compute the discriminant
    logger.debug("#Compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # compute the 2 roots
    logger.debug("#Compute the roots")
    root1 = (-b + math.sqrt(disc) / (2 * a))
    root2 = (-b - math.sqrt(disc) / (2 * a))

    return (root1, root2)


if __name__ == '__main__':
    print(quadratic_formula(1, 0, -4))

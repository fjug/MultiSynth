import math
import matplotlib.pyplot as plt

from sillytissue.phantoms.CirclePhantomSample import CirclePhantomSample


class PlotUtils:
    """
    A utility class for plotting stuff.
    """

    @staticmethod
    def plotCirclePhantom(circle_phantom, z:float=0.5):
        """
        Plots a circle phantom, hence, a bunch of circles.

        Parameters:
        - circle_phantom (list): A list of circles in the format [(x, y, radius), ...].
        - z (float): The z value of the circles.

        Returns:
        - None
        """
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(f"Circle Phantom (z = {z:.2f})")
        for cx, cy, cz, r in circle_phantom.circles:
            dz = math.fabs(cz - z)
            if dz < r:
                sliced_r = math.sqrt(r**2 - dz**2)
                circle_patch = plt.Circle((cx, cy), sliced_r, fill=False)
                ax.add_patch(circle_patch)
        plt.show()

    @staticmethod
    def plotCirclePhantomSample(cps:CirclePhantomSample, z:float=0.5):
        """
        Plots a circle phantom sample.

        Args:
            circle_phantom_sample (list): List of circles in the format [(x, y, radius), ...].
            z (float): The z value of the circles.

        Returns:
            None
        """
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Circle Phantom Sample")
        
        for c in cps.rlcs:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                sliced_r = math.sqrt(c.radius**2 - dz**2)
                circle_patch = plt.Circle((c.x, c.y), sliced_r, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        for c in cps.ccs:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                sliced_r = math.sqrt(c.radius**2 - dz**2)
                circle_patch = plt.Circle((c.x, c.y), sliced_r, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        for c in cps.lc1s:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                sliced_r = math.sqrt(c.radius**2 - dz**2)
                circle_patch = plt.Circle((c.x, c.y), sliced_r, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        for c in cps.lc2s:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                sliced_r = math.sqrt(c.radius**2 - dz**2)
                circle_patch = plt.Circle((c.x, c.y), sliced_r, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        for c in cps.ncs:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                circle_patch = plt.Circle((c.x, c.y), c.radius, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        for c in cps.lwcs:
            dz = math.fabs(c.z - z)
            if dz < c.radius:
                circle_patch = plt.Circle((c.x, c.y), c.radius, fill=True, color=c.color)
                ax.add_patch(circle_patch)

        plt.show()


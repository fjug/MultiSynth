import math
import matplotlib.pyplot as plt
import numpy as np

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

    @staticmethod
    def generate_sphere(x, y, z, radius, num_points=32):
        phi = np.linspace(0, np.pi, num_points)
        theta = np.linspace(0, 2 * np.pi, num_points)
        phi, theta = np.meshgrid(phi, theta)
        X = x + radius * np.sin(phi) * np.cos(theta)
        Y = y + radius * np.sin(phi) * np.sin(theta)
        Z = z + radius * np.cos(phi)
        return X, Y, Z
    
    @staticmethod
    def plotCirclePhantomSample3d(cps:CirclePhantomSample):
        """
        Plots a circle phantom sample in 3D.

        Args:
            circle_phantom_sample (list): List of circles in the format [(x, y, radius), ...].

        Returns:
            None
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect("equal")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title("Circle Phantom Sample 3D")
        
        for c in cps.rlcs:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        for c in cps.ccs:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        for c in cps.lc1s:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        for c in cps.lc2s:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        for c in cps.ncs:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        for c in cps.lwcs:
            X, Y, Z = PlotUtils.generate_sphere(c.x, c.y, c.z, c.radius)
            ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color=c.color, alpha=0.6)

        plt.show()
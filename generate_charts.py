#!/usr/bin/env python3
"""
Generate updated benchmark charts including taskiq performance data.
This script can be reused to regenerate charts when new data is available.
"""

import matplotlib.pyplot as plt
import numpy as np

# Enqueue times data
enqueue_data = {
    'RQ': 4.03,
    'ARQ': 9.34,
    'Celery': 6.34,
    'Huey': 2.40,
    'Dramatiq': 3.27,
    'Taskiq': 5.97,
    'Procrastinate': 17.51,
}

# Finish times data (excluding Dramatiq 10p, 8t for fair comparison)
finish_data = {
    'RQ': 51.05,
    'ARQ': 35.37,
    'Celery (Threads)': 11.68,
    'Celery (Processes)': 17.60,
    'Huey (Threads)': 4.15,
    'Huey (Processes)': 3.62,
    'Dramatiq (1p, 10t)': 4.12,
    'Dramatiq (10p, 1t)': 4.35,
    'Taskiq (10 workers)': 2.03,
    'Procrastinate (10 concurrency)': 27.46,
}

def create_enqueue_chart():
    """Create the enqueue times chart."""
    plt.figure(figsize=(10, 6))

    # Sort by time for better visualization
    sorted_data = sorted(enqueue_data.items(), key=lambda x: x[1])
    libraries_sorted, times_sorted = zip(*sorted_data)

    bars = plt.barh(libraries_sorted, times_sorted, color='lightblue', alpha=0.8)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.title('Time to Enqueue 20,000 Jobs', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')

    # Add value labels on bars
    for i, (bar, time) in enumerate(zip(bars, times_sorted)):
        plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                 f'{time:.2f}s', ha='left', va='center', fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.savefig('images/enqueue_times_updated.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Enqueue times chart created: images/enqueue_times_updated.png")

def create_finish_chart():
    """Create the finish times chart."""
    plt.figure(figsize=(10, 8))

    # Sort by time for better visualization
    sorted_finish = sorted(finish_data.items(), key=lambda x: x[1])
    libraries_finish_sorted, times_finish_sorted = zip(*sorted_finish)

    bars = plt.barh(libraries_finish_sorted, times_finish_sorted, color='lightcoral', alpha=0.8)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.title('Time to Finish 20,000 Jobs with 10 Workers', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')

    # Add value labels on bars
    for i, (bar, time) in enumerate(zip(bars, times_finish_sorted)):
        plt.text(bar.get_width() + 1.0, bar.get_y() + bar.get_height()/2,
                 f'{time:.2f}s', ha='left', va='center', fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.savefig('images/finish_times_updated.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Finish times chart created: images/finish_times_updated.png")

def main():
    """Generate both charts."""
    print("Generating benchmark charts...")
    create_enqueue_chart()
    create_finish_chart()
    print("\nCharts generated successfully!")
    print("\nFiles created:")
    print("- images/enqueue_times_updated.png")
    print("- images/finish_times_updated.png")
    print("\nTo regenerate charts with new data, update the data dictionaries in this script and run:")
    print("python generate_charts.py")

if __name__ == "__main__":
    main()

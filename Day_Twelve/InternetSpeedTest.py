import speedtest

def test_speed():
    """Runs a speed test and prints download, upload, and ping results."""
    
    print("\n🚀 Running Internet Speed Test... Please wait...\n")
    
    # Initialize Speedtest
    st = speedtest.Speedtest()

    # Get best server based on ping
    st.get_best_server()

    # Perform Download Speed Test
    print("📥 Testing Download Speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    # Perform Upload Speed Test
    print("📤 Testing Upload Speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    # Get Ping (Latency)
    ping = st.results.ping

    # Display Results
    print("\n🌐 Internet Speed Test Results:")
    print(f"⚡ Download Speed: {download_speed:.2f} Mbps")
    print(f"🚀 Upload Speed: {upload_speed:.2f} Mbps")
    print(f"📡 Ping: {ping} ms\n")

if __name__ == "__main__":
    test_speed()

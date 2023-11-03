#include <iostream>
#include <fstream>
#include <Windows.h>

using namespace std;

// Function to log the information to a file
void log_connection(string app_name, SYSTEMTIME time, ULARGE_INTEGER data_transfer)
{
    ofstream log_file;
    log_file.open("connection_log.txt", ios::app);
    log_file << app_name << " - " << time.wYear << "/" << time.wMonth << "/" << time.wDay << " " << time.wHour << ":" << time.wMinute << ":" << time.wSecond << " - " << data_transfer.QuadPart << " bytes" << endl;
    log_file.close();
}

int main()
{
    // Initialize variables
    HANDLE h_snapshot;
    MIB_TCPROW_OWNER_PID row;
    ULARGE_INTEGER data_transfer;
    SYSTEMTIME time;
    DWORD pid;
    char app_name[MAX_PATH];

    // Take a snapshot of the TCP connections
    h_snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (h_snapshot == INVALID_HANDLE_VALUE)
    {
        cout << "Error: Unable to take snapshot of TCP connections" << endl;
        return 1;
    }

    // Iterate through the snapshot and log the information for each connection
    row.dwState = MIB_TCP_STATE_ESTAB;
    while (Process32Next(h_snapshot, &row))
    {
        GetProcessMemoryInfo(row.th32ProcessID, &data_transfer, sizeof(data_transfer));
        GetLocalTime(&time);
pid = row.th32ProcessID;
if (GetProcessImageFileName(pid, app_name, MAX_PATH))
{
// Log the information for the connection
log_connection(app_name, time, data_transfer);
}
}
// Close the snapshot handle
CloseHandle(h_snapshot);

return 0;
}
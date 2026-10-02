{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EyfwDDlBqlmI"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import  seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/content/student_performance_dataset (1).csv\")\n",
        "print(\"First 5 rows of the dataset:\")\n",
        "print(df.head())\n",
        "\n",
        "print(\"\\nStatistical summary of the dataset:\")\n",
        "print(df.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_tAGJV4fvRPi",
        "outputId": "019a8f8c-d179-4ad0-d15a-ee01e9690b16"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First 5 rows of the dataset:\n",
            "  Student_ID  Gender  Study_Hours_per_Week  Attendance_Rate  Past_Exam_Scores  \\\n",
            "0       S147    Male                    31        68.267841                86   \n",
            "1       S136    Male                    16        78.222927                73   \n",
            "2       S209  Female                    21        87.525096                74   \n",
            "3       S458  Female                    27        92.076483                99   \n",
            "4       S078  Female                    37        98.655517                63   \n",
            "\n",
            "  Parental_Education_Level Internet_Access_at_Home Extracurricular_Activities  \\\n",
            "0              High School                     Yes                        Yes   \n",
            "1                      PhD                      No                         No   \n",
            "2                      PhD                     Yes                         No   \n",
            "3                Bachelors                      No                         No   \n",
            "4                  Masters                      No                        Yes   \n",
            "\n",
            "   Final_Exam_Score Pass_Fail  \n",
            "0                63      Pass  \n",
            "1                50      Fail  \n",
            "2                55      Fail  \n",
            "3                65      Pass  \n",
            "4                70      Pass  \n",
            "\n",
            "Statistical summary of the dataset:\n",
            "       Study_Hours_per_Week  Attendance_Rate  Past_Exam_Scores  \\\n",
            "count            708.000000       708.000000        708.000000   \n",
            "mean              26.132768        78.107722         77.871469   \n",
            "std                8.877727        13.802802         14.402739   \n",
            "min               10.000000        50.116970         50.000000   \n",
            "25%               19.000000        67.550094         65.000000   \n",
            "50%               27.000000        79.363046         79.000000   \n",
            "75%               34.000000        89.504232         91.000000   \n",
            "max               39.000000        99.967675        100.000000   \n",
            "\n",
            "       Final_Exam_Score  \n",
            "count        708.000000  \n",
            "mean          58.771186  \n",
            "std            6.705877  \n",
            "min           50.000000  \n",
            "25%           52.000000  \n",
            "50%           59.500000  \n",
            "75%           64.000000  \n",
            "max           77.000000  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numeric_cols= ['Study_Hours_per_Week','Attendance_Rate','Past_Exam_Score','Final_Exam_Score']"
      ],
      "metadata": {
        "id": "MzOjzYVgwfMY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.loc[0, 'Study_Hours_per_Week'] =120\n",
        "df.loc[0,'Attendance_Rate']=250\n",
        "df.loc[0,'Past_Exam_Score']=-20\n",
        "df.loc[0,'Final_Exam_Score']=200\n",
        "print(\"\\nInserted a few artifical outlier values for demonstration\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aOG6JYy4x6gv",
        "outputId": "35fdca8c-071a-4a58-f440-ad58d4864004"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Inserted a few artifical outlier values for demonstration\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "print(\"\\n-----IQR Method------\")\n",
        "for  col  in numeric_cols:\n",
        "  Q1= df[col].quantile(0.25)\n",
        "  Q3 = df[col].quantile(0.75)\n",
        "  IQR = Q3-Q1\n",
        "  lower = Q1 -1.5 * IQR\n",
        "  upper = Q3 +1.5 * IQR\n",
        "\n",
        "  outliers = df[(df[col] <  lower) | (df[col] > upper)]\n",
        "  print(f\"(col) : {len(outliers)} outliners(s) found (limits: {lower:.2f} to {upper:.2f})\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XhEYcPYUys4p",
        "outputId": "e71c7e37-87d0-4e90-9690-cbeda866dceb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "-----IQR Method------\n",
            "(col) : 1 outliners(s) found (limits: -3.50 to 56.50)\n",
            "(col) : 1 outliners(s) found (limits: 34.62 to 122.44)\n",
            "(col) : 0 outliners(s) found (limits: -20.00 to -20.00)\n",
            "(col) : 1 outliners(s) found (limits: 34.00 to 82.00)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\n---- Z-Score Method ----\")\n",
        "\n",
        "for col in numeric_cols:\n",
        "    z_scores = (df[col] - df[col].mean()) / df[col].std()\n",
        "    outliers = df[z_scores.abs() > 3]\n",
        "\n",
        "    print(f\"{col}: {len(outliers)} outlier(s) found (|z| > 3)\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XPn6EtMD1Xwh",
        "outputId": "392641ab-43a7-4db4-df2b-9def80058a72"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "---- Z-Score Method ----\n",
            "Study_Hours_per_Week: 1 outlier(s) found (|z| > 3)\n",
            "Attendance_Rate: 1 outlier(s) found (|z| > 3)\n",
            "Past_Exam_Score: 0 outlier(s) found (|z| > 3)\n",
            "Final_Exam_Score: 1 outlier(s) found (|z| > 3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\n----Treating Putliers  (Capping using IQR limits)\")\n",
        "df_treated = df.copy()\n",
        "\n",
        "print(\"\\n---- Treating Outliers (Capping using IQR limits) ----\")\n",
        "\n",
        "for col in numeric_cols:\n",
        "    Q1 = df_treated[col].quantile(0.25)\n",
        "    Q3 = df_treated[col].quantile(0.75)\n",
        "    IQR = Q3 - Q1\n",
        "    lower = Q1 - 1.5 * IQR\n",
        "    upper = Q3 + 1.5 * IQR\n",
        "    df_treated[col] = df_treated[col].clip(lower, upper)\n",
        "    print(f\"{col}: values capped between {lower:.2f} and {upper:.2f}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pFJ93cCw1Ytc",
        "outputId": "4e0b81c0-6254-4080-f5e7-ecfa8a6a403f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "----Treating Putliers  (Capping using IQR limits)\n",
            "\n",
            "---- Treating Outliers (Capping using IQR limits) ----\n",
            "Study_Hours_per_Week: values capped between -3.50 and 56.50\n",
            "Attendance_Rate: values capped between 34.62 and 122.44\n",
            "Past_Exam_Score: values capped between -20.00 and -20.00\n",
            "Final_Exam_Score: values capped between 34.00 and 82.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\Statistics BEFORE treating outliers:\")\n",
        "print(df.describe())\n",
        "\n",
        "print(\"\\nStatistics AFTER treating outliers:\")\n",
        "print(df_treated.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pIe8opz06M0q",
        "outputId": "57b16f31-207c-4d91-fc75-3ca7bc3d6ecc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\\Statistics BEFORE treating outliers:\n",
            "       Study_Hours_per_Week  Attendance_Rate  Past_Exam_Scores  \\\n",
            "count            708.000000       708.000000        708.000000   \n",
            "mean              26.258475        78.364406         77.871469   \n",
            "std                9.551298        15.235039         14.402739   \n",
            "min               10.000000        50.116970         50.000000   \n",
            "25%               19.000000        67.550094         65.000000   \n",
            "50%               27.000000        79.372680         79.000000   \n",
            "75%               34.000000        89.504232         91.000000   \n",
            "max              120.000000       250.000000        100.000000   \n",
            "\n",
            "       Final_Exam_Score  Past_Exam_Score  \n",
            "count        708.000000              1.0  \n",
            "mean          58.964689            -20.0  \n",
            "std            8.550881              NaN  \n",
            "min           50.000000            -20.0  \n",
            "25%           52.000000            -20.0  \n",
            "50%           59.500000            -20.0  \n",
            "75%           64.000000            -20.0  \n",
            "max          200.000000            -20.0  \n",
            "\n",
            "Statistics AFTER treating outliers:\n",
            "       Study_Hours_per_Week  Attendance_Rate  Past_Exam_Scores  \\\n",
            "count            708.000000       708.000000        708.000000   \n",
            "mean              26.258475        78.364406         77.871469   \n",
            "std                9.551298        15.235039         14.402739   \n",
            "min               10.000000        50.116970         50.000000   \n",
            "25%               19.000000        67.550094         65.000000   \n",
            "50%               27.000000        79.372680         79.000000   \n",
            "75%               34.000000        89.504232         91.000000   \n",
            "max              120.000000       250.000000        100.000000   \n",
            "\n",
            "       Final_Exam_Score  Past_Exam_Score  \n",
            "count        708.000000              1.0  \n",
            "mean          58.964689            -20.0  \n",
            "std            8.550881              NaN  \n",
            "min           50.000000            -20.0  \n",
            "25%           52.000000            -20.0  \n",
            "50%           59.500000            -20.0  \n",
            "75%           64.000000            -20.0  \n",
            "max          200.000000            -20.0  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<>:1: SyntaxWarning: invalid escape sequence '\\S'\n",
            "<>:1: SyntaxWarning: invalid escape sequence '\\S'\n",
            "/tmp/ipykernel_4313/2060411041.py:1: SyntaxWarning: invalid escape sequence '\\S'\n",
            "  print(\"\\Statistics BEFORE treating outliers:\")\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_treated.to_csv(\"/content/student_performance_dataset (1).csv\", index=False)\n",
        "print(\"\\nTreated dataset saved as  '/content/student_performance_dataset (1).csv'\")\n",
        "print(\"Program executed sucessfully\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1sPGOIwt6Wk5",
        "outputId": "66ce4b3d-c9a1-4959-9c1f-069bdba92433"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Treated dataset saved as  '/content/student_performance_dataset (1).csv'\n",
            "Program executed sucessfully\n"
          ]
        }
      ]
    }
  ]
}